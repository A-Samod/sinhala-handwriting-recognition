const express = require('express');
const multer = require('multer');
const tf = require('@tensorflow/tfjs-node');
const fs = require('fs');
const app = express();

const upload = multer({ dest: 'uploads/' });

const sinhalaClasses = ["අ", "ක", "ග"];

let model;

// Load the model
tf.loadLayersModel('file://path/to/web_model/model.json').then((loadedModel) => {
  model = loadedModel;
});

// Image preprocessing
function preprocessImage(filePath) {
  const imageBuffer = fs.readFileSync(filePath);
  const imageTensor = tf.node.decodeImage(imageBuffer, 1)
    .resizeNearestNeighbor([80, 80])
    .expandDims(0)
    .toFloat()
    .div(255.0);
  return imageTensor;
}

// Route for prediction
app.post('/predict', upload.single('image'), async (req, res) => {
  if (!model) {
    return res.status(500).send("Model not loaded yet.");
  }

  const imageTensor = preprocessImage(req.file.path);
  const predictions = model.predict(imageTensor);
  const predictedClass = predictions.argMax(-1).dataSync()[0];

  res.json({ predicted_letter: sinhalaClasses[predictedClass] });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});