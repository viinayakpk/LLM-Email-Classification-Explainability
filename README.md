# LLM-Powered Email Classification with Explainability

## Overview
This project implements a secure Natural Language Processing (NLP) pipeline for **phishing email detection** using a **DistilBERT-based** classifier. The model is integrated with **SHAP** (SHapley Additive exPlanations) to provide **token-level interpretability** for the predictions. The backend is built with **FastAPI** for real-time inference, and the entire system is **containerized using Docker** for easy deployment.

The system aims to classify emails as either "phishing" or "ham" (non-phishing) with **92% F1 score** on a custom dataset.

## Tech Stack
- **Model**: DistilBERT (HuggingFace Transformers)
- **Explainability**: SHAP
- **Backend**: FastAPI (for real-time API deployment)
- **Containerization**: Docker
- **Others**: pandas, scikit-learn, uvicorn, torch

## Features
- **Real-time Phishing Detection**: Detect phishing emails with high accuracy.
- **Explainability**: Token-level explanation of predictions using SHAP.
- **Easy Deployment**: Dockerized application for seamless local and cloud deployment.
- **Model Evaluation**: Trained on a custom dataset with a **92% F1 score**.

## Project Structure
