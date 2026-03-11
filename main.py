from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from predictor import predict_disease
from treatment import treatment_data

app = FastAPI()

# Static folder (CSS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Run AI model
    disease, confidence = predict_disease(file.file)

    # Get treatment
    treatment = treatment_data.get(disease, "No treatment available")

    return {
        "Disease": disease,
        "Confidence": confidence,
        "Treatment": treatment
    }