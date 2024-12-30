# Repository for final project

# Emotion Detection Application

This project is an AI-powered web application for detecting emotions in text. It uses the **Watson NLP Library** to analyze the input and return the corresponding emotions with their respective scores. The application is developed with Flask and incorporates features such as error handling and a user-friendly interface.

---

## Features

- Detect emotions such as **anger**, **disgust**, **fear**, **joy**, and **sadness**.
- Display the dominant emotion for the provided text.
- Error handling for invalid or blank inputs.
- Simulated responses for offline testing.
- RESTful API endpoint for integrating with other applications.

---

## Project Structure

```plaintext
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
├── static/
│   ├── mywebscript.js
├── templates/
│   ├── index.html
├── server.py
├── test_emotion_detection.py
├── README.md
├── LICENSE
└── .gitignore
```

## Prerequisites

- Python 3.12 or higher
- Flask
- PyLint
- Postman (For API testing)

  ## Installation

1. Clone the repository
```
git clone https://github.com/AIExxplorer/final_project.git cd final_project
```
2. Set up a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required packages
```
pip install -r requirements.txt
```


## Usage

### Running the Application
1. Start the Flask Server
```
python server.py
```

2. Open your browser and navigate to http://127.0.0.1:5000

### Testing the Application
- Use Postman to test the /emotionDetector endpoint.
- Example JSON body:"
```
{
  "text": "I think I am having fun"
}
```
-  Expected output:"
```
{
  "anger": 0.0,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.99,
  "sadness": 0.01,
  "dominant_emotion": "joy"
}
```

## Error Handling 
- If no input is provided, the system will return:
```
{
  "error": "Invalid text! Please try again!"
}
```

## Testing
- Run the unit tests:
```
python -m unittest test_emotion_detection.py
```
- Check the output for all test passing.

## Code Quality
- Run static code analysis with PyLint:
```
pylint server.py
```
- Ensure a score of 10/10 for clean and maintainable code.

## License
- This project is licensed under the APACHE License for more details click under LICENSE at the top right of the repository.

## Acknowledgments
- IBM Watson NLP Library for enabling the emotion detection funcionality.
- Flask for simplifying the web application development.
