# My-Projects
# Introduction
Depression is one of the most common mental health challenges in today’s digital era, and early detection is crucial for effective intervention. With the rise of social media, users often express emotions and moods through text and images that can reflect their mental well-being. This project, Depression Detection on Social Media, aims to leverage artificial intelligence to automatically identify signs of depression from users’ text posts and facial expressions. The system integrates deep learning and natural language processing techniques to analyze multimodal data and predict depression risk in real time.
# Project Description
The Depression Detection on Social Media system is a real-time AI-powered web application built using Flask, combining both facial emotion recognition and text sentiment analysis to detect potential depression levels in users. It utilizes Convolutional Neural Networks (CNN) for analyzing facial expressions from uploaded images and NLP models (using NLTK and spaCy) for interpreting the emotional tone of text-based social media posts. A rule-based fusion algorithm consolidates both results to produce a final depression risk score. The web app provides role-based access for users and administrators—users can upload data and view their depression analysis results, while admins can monitor user activity, risk levels, and historical trends. All data is securely stored in a MySQL database, ensuring privacy and reliability. The system also includes therapy suggestions and consultation recommendations, offering a supportive interface that bridges AI technology and mental health care.
# Technology Stack
Programming Language: Python
Web Framework: Flask
Deep Learning Library: TensorFlow / Keras
Natural Language Processing: NLTK, spaCy
Computer Vision: OpenCV
Database: MySQL (via XAMPP)
Frontend: HTML, CSS, JavaScript
Model Files: CNN model (depression_cnn_model.h5) and NLP model (nlp_sentiment_model.pkl)
# Installation Guidelines
# Clone the Repository
git clone https://github.com/yourusername/depression-detection-social-media.git
cd depression-detection-social-media
# Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate  # (Windows)
# Install the Required Packages
pip install -r requirements.txt
# Import the Database
Open XAMPP or MySQL Workbench
Create a new database named depression_db
Import the provided depression_db.sql file
# Run the Application
python app.py
# Configuration
Database Configuration:
Update your database credentials in app.py if needed:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'depression_db'
# Model Configuration:
Place your pre-trained models (depression_cnn_model.h5 and nlp_sentiment_model.pkl) in the project’s root directory.
# Default Admin Credentials:
Username: admin  
Password: password
