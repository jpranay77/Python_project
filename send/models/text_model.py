from transformers import pipeline

# Hugging Face sentiment pipeline
nlp = pipeline("sentiment-analysis")

def analyze_text(text):
    result = nlp(text)[0]
    # Convert NEGATIVE sentiment into depression risk
    if result['label'] == 'NEGATIVE':
        return min(result['score'] + 0.3, 1.0)  # scale up
    else:
        return max(0.0, 1 - result['score'])
