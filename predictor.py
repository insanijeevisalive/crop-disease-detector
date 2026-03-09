import random

diseases = [
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Healthy Leaf",
    "Corn Leaf Spot"
]

def predict_disease():
    return random.choice(diseases)