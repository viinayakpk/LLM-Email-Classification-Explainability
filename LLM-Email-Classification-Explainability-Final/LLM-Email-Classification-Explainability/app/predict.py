from transformers import pipeline

# Load the pre-trained model and tokenizer from HuggingFace (use a fine-tuned model in practice)
classifier = pipeline("text-classification", model="distilbert-base-uncased", return_all_scores=True)

def predict_email(text: str):
    prediction = classifier(text)
    label = prediction[0][1]["label"]  # 1 represents 'phishing'
    return {"label": label}
