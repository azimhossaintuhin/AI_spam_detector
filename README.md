# Spam Checker API

A minimal FastAPI service that wraps a local Hugging Face text-classification model to detect spam messages. The model and tokenizer are stored in `spam_model/`, so the API runs fully offline.

![Spam Detection UI](./Spam%20Detection.png)

## Requirements
- Python 3.10+
- pip

## Setup
1) Create and activate a virtual environment (recommended):
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2) Install dependencies:
```powershell
pip install fastapi uvicorn[standard] transformers torch
```

## Running the API
Start the server with Uvicorn from the project root:
```powershell
uvicorn main:app --reload
```

The server will listen on `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Endpoint
`POST /predict`
- **Body**: `{ "text": "Your message here" }`
- **Response**: `{ "label": "SPAM" | "NOT SPAM", "score": <float confidence> }`

Example using PowerShell:
```powershell
$body = @{ text = "Congratulations! You won a prize" } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/predict -Method Post -Body $body -ContentType "application/json"
```

Example using curl:
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello, this is a test message."}'
```

## Model Notes
- The service loads a local text-classification pipeline from `spam_model/` using `transformers.pipeline` on CPU.
- Output labels from the model are mapped to `SPAM` when the raw label is `LABEL_1`; everything else is treated as `NOT SPAM`.

## Development
- Adjust thresholds or label mapping in `main.py` inside the `/predict` handler.
- Regenerate or swap the model by replacing the files in `spam_model/` with a compatible text-classification checkpoint.

## Project Story
I built this as a beginner-friendly experiment to see how data, AI models, and APIs connect end-to-end:
- Dataset: SMS Spam dataset from Hugging Face.
- Model: DistilBERT fine-tuned with Python + PyTorch for lightweight spam/ham detection.
- Serving: A small FastAPI endpoint (`POST /predict`) that responds in real time with `SPAM` or `NOT SPAM`.

It is intentionally simple, but it helped me understand the full flow: prep data → train → save artifacts → serve via API → try live requests. If you are also learning AI and want to explore or collaborate, the code lives here: https://github.com/azimhossaintuhin/AI_spam_detector
