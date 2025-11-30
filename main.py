from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch

app = FastAPI()

classifier = pipeline(
    "text-classification",
    model="spam_model",
    tokenizer="spam_model",
    device_map="cpu"
)

print("Model loaded and ready.")


class Message(BaseModel):
    text: str

@app.post("/predict")
def predict(msg: Message):
    result = classifier(msg.text)[0]
    label = "SPAM" if result["label"] == "LABEL_1" else "NOT SPAM"
    return {"label": label, "score": float(result["score"])}
