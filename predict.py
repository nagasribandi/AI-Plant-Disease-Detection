import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json

# Load model
model = tf.keras.models.load_model("models/plant_disease_model.keras")

# Load class names
with open("class_names.json") as f:
    class_names = json.load(f)

IMG_SIZE = (224, 224)

def predict_disease(uploaded_file):

    img = image.load_img(uploaded_file, target_size=IMG_SIZE)

    img_array = image.img_to_array(img)

    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]

    # Get top 5 prediction indexes
    top5_idx = prediction.argsort()[-5:][::-1]

    results = []

    for i in top5_idx:
        disease = class_names[i]
        confidence = float(prediction[i] * 100)
        results.append((disease, confidence))
  
    return results