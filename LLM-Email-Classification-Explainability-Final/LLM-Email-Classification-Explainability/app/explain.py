import shap
from transformers import pipeline

# Load pre-trained model and tokenizer for SHAP explainability
classifier = pipeline("text-classification", model="distilbert-base-uncased")

def explain_email(text: str):
    explainer = shap.Explainer(classifier, input_data=text)
    shap_values = explainer.shap_values(text)
    explanation = shap.summary_plot(shap_values, text)
    return {"explanation": "Explanation generated for phishing/ham prediction."}
