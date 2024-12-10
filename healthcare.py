import os
import ssl
import nltk
import random
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL Setup for NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# Healthcare-specific intents
intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "Good morning", "Good evening"],
        "responses": ["Hello! How can I assist you today?", "Hi there! Do you have any health-related questions?"]
    },
    {
        "tag": "symptoms",
        "patterns": ["I have a headache", "What should I do for fever?", "I'm feeling dizzy", "My stomach hurts"],
        "responses": ["Please ensure you stay hydrated and rest. If symptoms persist, consider consulting a doctor.", 
                      "It’s best to monitor your symptoms. Over-the-counter medicine might help, but seek medical advice if needed."]
    },
    {
        "tag": "treatment",
        "patterns": ["What is the treatment for a cold?", "How do I cure a sore throat?", "Is there a remedy for back pain?"],
        "responses": ["For a cold, rest and drink plenty of fluids. If it lasts over a week, consult a doctor.", 
                      "Gargle with warm salt water for a sore throat, and stay hydrated."]
    },
    {
        "tag": "appointment",
        "patterns": ["How can I book an appointment?", "I need to see a doctor", "Can you schedule a visit for me?"],
        "responses": ["To book an appointment, please call your local clinic or visit their website.", 
                      "I recommend contacting your preferred healthcare provider for scheduling."]
    },
    {
        "tag": "nutrition",
        "patterns": ["What are healthy foods?", "Can you recommend a good diet?", "How can I eat healthier?"],
        "responses": ["A balanced diet includes fruits, vegetables, whole grains, lean protein, and healthy fats.", 
                      "Try to limit processed foods and include more fresh ingredients in your meals."]
    },
    {
        "tag": "mental_health",
        "patterns": ["I'm feeling stressed", "What should I do if I feel anxious?", "I think I need mental health help"],
        "responses": ["It's important to talk to someone you trust or a mental health professional.", 
                      "Practicing mindfulness, regular exercise, and deep breathing can help manage stress."]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "Goodbye", "See you", "Take care"],
        "responses": ["Goodbye! Take care and stay healthy.", "See you! Wishing you good health."]
    },
]

# Preparing the data for model training
patterns = []
tags = []
for intent in intents:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Text vectorization and model setup
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)
y = tags

# Train the classifier
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X, y)

# Chatbot logic
def chatbot_response(user_input):
    vectorized_input = vectorizer.transform([user_input])
    tag = model.predict(vectorized_input)[0]
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Streamlit app
def main():
    st.title("Healthcare Chatbot")
    st.write("Hi, I'm your healthcare assistant. Ask me anything related to health or appointments.")

    user_input = st.text_input("You:", key="user_input")

    if user_input:
        response = chatbot_response(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None)

        if response.lower() in ['goodbye', 'see you', 'take care']:
            st.write("Thank you for chatting with me. Stay healthy!")
            st.stop()

if __name__ == "__main__":
    main()
