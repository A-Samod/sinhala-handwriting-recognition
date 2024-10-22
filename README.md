# Sinhala Handwriting Recognition

This project is an Express.js server that utilizes TensorFlow.js to recognize Sinhala handwritten characters from uploaded images. It uses a pre-trained model to classify images into one of the Sinhala characters it has been trained on.

## Features
- Accepts image uploads via an API endpoint.
- Preprocesses images and predicts Sinhala characters using a TensorFlow.js model.
- Provides real-time predictions for Sinhala handwriting.

## Tech Stack
- **Express.js**: Web server framework.
- **Multer**: Middleware for handling image uploads.
- **TensorFlow.js**: For model loading and prediction.
- **Node.js**: Runtime environment.
- **fs**: File system operations to read uploaded images.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/sinhala-handwriting-recognition.git
    ```
    
2. Navigate to the project directory:
    ```bash
    cd sinhala-handwriting-recognition
    ```

3. Install the dependencies:
    ```bash
    npm install
    ```

4. Place your TensorFlow.js model files in the correct directory (`path/to/web_model` in the code).

5. Run the server:
    ```bash
    npm start
    ```

## API Endpoints

### POST `/predict`
- **Description**: Accepts an image file and returns the predicted Sinhala letter.
- **Body**: Multipart form-data with an `image` field.
- **Response**: 
    ```json
    {
      "predicted_letter": "ක"
    }
    ```

## Example Request

Using `curl`:
```bash
curl -X POST -F "image=@/path/to/image.png" http://localhost:3000/predict
