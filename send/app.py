from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_connection
from models.text_model import analyze_text
from models.facial_emotion import analyze_face

app = Flask(__name__)
app.secret_key = "depression_secret_key"

# -------- Landing --------
@app.route('/')
def index():
    return render_template("index.html")

# -------- Register --------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username,password,role) VALUES (%s,%s,%s)", 
                    (username,password,"user"))
        conn.commit()
        cur.close()
        conn.close()
        flash("Registered successfully, please login")
        return redirect(url_for('login'))
    return render_template("register.html")

# -------- Login --------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['role'] = user['role']
            if user['role'] == 'admin':
                return redirect(url_for('dashboard_admin'))
            else:
                return redirect(url_for('dashboard_user'))
        else:
            flash("Invalid credentials")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# -------- User Dashboard --------
@app.route('/dashboard_user', methods=['GET','POST'])
def dashboard_user():
    if 'user_id' not in session or session['role'] != 'user':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        text = request.form['post_text']
        text_score = analyze_text(text)
        face_score = analyze_face()
        risk = (0.6 * text_score) + (0.4 * face_score)
        
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO analyses (user_id,post_text,text_score,face_score,risk_score) VALUES (%s,%s,%s,%s,%s)",
                    (session['user_id'], text, text_score, face_score, risk))
        conn.commit()
        cur.close()
        conn.close()
        
        if risk > 0.7:
            return render_template("alert.html", risk=risk)
        return render_template("dashboard_user.html", result=True, text=text, text_score=text_score, face_score=face_score, risk=risk)
    
    return render_template("dashboard_user.html")

# -------- Admin Dashboard --------
@app.route('/dashboard_admin')
def dashboard_admin():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT a.id, u.username, a.post_text, a.risk_score, a.created_at FROM analyses a JOIN users u ON a.user_id=u.id ORDER BY a.created_at DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template("dashboard_admin.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
