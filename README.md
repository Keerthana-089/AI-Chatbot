# AI Voice Chatbot

## Overview

AI Voice Chatbot is a Python-based conversational assistant capable of responding to user queries using natural language processing.
The chatbot supports both text-based and voice-based interaction, allowing users to communicate with the system through speech or typed input.

The system uses machine learning techniques to classify user intents and generate appropriate responses.

---

## Features

* Natural Language Processing based chatbot
* Intent classification using machine learning
* Voice input using microphone
* Text-to-speech response generation
* Web-based chatbot interface
* Local voice assistant functionality

---

## Project Structure

```
AI-Chatbot
│
├── chatbot.py            # Core chatbot logic
├── train.py              # Model training script
├── intents.json          # Intent dataset for chatbot
│
├── voice_ai_chatbot.py   # Voice-enabled chatbot
├── voice_ai_local.py     # Local voice assistant version
│
├── mic_test.py           # Microphone input testing
├── tts_test.py           # Text-to-speech testing
│
├── web_chatbot.py        # Web interface for chatbot
│
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # Text vectorizer
│
└── requirements.txt      # Project dependencies
```

---

## Technologies Used

* Python
* Natural Language Processing (NLP)
* Scikit-learn
* Speech Recognition
* Text-to-Speech
* Machine Learning

---

## Installation

Clone the repository:

```
git clone https://github.com/Keerthana-089/AI-Chatbot.git
```

Navigate to the project directory:

```
cd AI-Chatbot
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Chatbot

Run the basic chatbot:

```
python chatbot.py
```

Run the voice chatbot:

```
python voice_ai_chatbot.py
```

Run the web chatbot:

```
python web_chatbot.py
```

---

## Future Improvements

* Add deep learning based NLP models
* Integrate external APIs for advanced responses
* Improve voice recognition accuracy
* Deploy chatbot as a web application

---

## Author

Keerthana C
B.Tech Computer Science Engineering
KLH University
