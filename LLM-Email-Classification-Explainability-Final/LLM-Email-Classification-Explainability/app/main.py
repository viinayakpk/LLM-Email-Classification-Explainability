from fastapi import FastAPI
from app.predict import predict_email
from app.explain import explain_email

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LLM Email Classification API"}

@app.post("/predict")
def classify_email(text: str):
    return predict_email(text)

@app.post("/explain")
def explain(text: str):
    return explain_email(text)
