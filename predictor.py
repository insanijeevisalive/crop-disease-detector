import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("plant_disease_model.h5")

classes = [
"Tomato Early Blight",
"Tomato Late Blight",
"Tomato Healthy",
"Tomato Leaf Mold",
"Tomato Septoria Leaf Spot"
]

def predict_disease(image_file):

    img = Image.open(image_file)
    img = img.resize((224,224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    index = np.argmax(prediction)

    confidence = float(prediction[0][index]) * 100

    return classes[index], round(confidence,2)