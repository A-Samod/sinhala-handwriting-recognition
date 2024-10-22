# 

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
import tempfile

app = Flask(__name__)

# Load your pre-trained model
model = tf.keras.models.load_model('model_test_v1.h5')

# Sinhala classes
sinhala_classes = ["අ", "ක", "ග"]

def prepare_image(img_data):
    img_array = image.img_to_array(img_data)
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']
    
    # Save the file to a temporary location
    temp_file_path = os.path.join(tempfile.gettempdir(), file.filename)
    file.save(temp_file_path)

    # Load the image from the saved file
    img = image.load_img(temp_file_path, target_size=(80, 80), color_mode="grayscale")
    img_array = prepare_image(img)

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    predicted_letter = sinhala_classes[predicted_class[0]]

    # Remove the temporary file after prediction
    os.remove(temp_file_path)

    return jsonify({"predicted_letter": predicted_letter})

if __name__ == '__main__':
    app.run(debug=True)