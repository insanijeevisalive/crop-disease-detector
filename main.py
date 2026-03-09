from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from predictor import predict_disease
from treatment import treatment_data

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html") as f:
        return f.read()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    disease = predict_disease()
    solution = treatment_data[disease]

    return {
        "Disease": disease,
        "Treatment": solution
    }