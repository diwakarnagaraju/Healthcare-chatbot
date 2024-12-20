# Healthcare Chatbot

A smart and interactive chatbot designed to assist users with healthcare-related queries, providing quick and accurate information on symptoms, treatments, and nearby healthcare facilities.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Images](#images).
6. [Project Structure](#project-structure)
7. [API Integration](#api-integration)
8. [Future Enhancements](#future-enhancements)
9. [Contact](#contact)

---

## Features

- Symptom checker based on user input.
- Provides health tips and first aid suggestions.
- Real-time connection to healthcare providers or resources.
- Integration with APIs for nearby hospitals and pharmacies.
- Multi-language support for better accessibility.
- User-friendly interface developed in Streamlit.

---

## Technologies Used

- **Python 3.11**
- **Streamlit**: For creating the interactive user interface.
- **TensorFlow/Keras**: For AI and machine learning models.
- **NLTK**: For natural language processing.
- **Flask**: For backend API integration.
- **SQLite**: For database management.

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/diwakarnagaraju/healthcare-chatbot.git
2. Navigate to the project directory:
   ```bash
   cd healthcare-chatbot
3. Create a virtual environment and activate it:
   `
  python -m venv venv
source venv/bin/activate # On Windows: `venv\Scripts\activate`

4. Install the required dependencies:
   ```
   pip install -r requirements.txt

5. Run the application:
   ```
   streamlit run healthcare_chatbot.py
---

## Usage

Start the chatbot by running the following command in your terminal:
   ```
   streamlit run healthcare_chatbot.py
   ```

Interact with the chatbot by typing your healthcare-related questions in the chat window. Examples include:

- "What are the symptoms of flu?"
- "Where can I find the nearest hospital?"
- "What should I do for a headache?"
- The chatbot provides instant responses, including:

- Symptom analysis.
- Health recommendations.
- Directions to nearby healthcare facilities.

---

## Images
- Greetings!
  ![Greetings](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/680716ade6620b90ae9acd8b00cb4602a82f5bce/greetings.png "Greetings")

- Symptoms
  ![symptoms](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/57a10b7d45c4d0badc2861b74a43da7aaf5f03d9/symptoms.png)

- Treatment
  ![treatment](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/e7abd4e2e6f68611101495c4e075f06d78785a43/treatment.png)

- Appointment
  ![appointment](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/e7abd4e2e6f68611101495c4e075f06d78785a43/appointment.png)

- Nutrition
  ![nutrition](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/e7abd4e2e6f68611101495c4e075f06d78785a43/nutrition.png)

- Mental Health
  ![Mental Health](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/e7abd4e2e6f68611101495c4e075f06d78785a43/Mental_health.png)

- Good Bye
  ![Good Bye](https://github.com/diwakarnagaraju/Healthcare-chatbot/blob/e7abd4e2e6f68611101495c4e075f06d78785a43/Goodbye.png)


## Project Structure

- healthcare-chatbot/
- ├── app.py                # Main application file
- ├── chatbot_model/        # Pre-trained chatbot models
- ├── data/                 # Training and testing datasets
- ├── templates/            # HTML templates (if any)
- ├── static/               # CSS, JS, images, etc.
- ├── README.md             # Project documentation
- └── requirements.txt      # Python dependencies

---

## API Integration

- Health APIs: Access health-related information (e.g., symptoms, treatments).
- Google Maps API: Locate nearby hospitals and pharmacies.
- Setup: Configure API keys by adding them to a .env file in the root directory.

---

## Future Enhancements

- Integration with wearable health devices for real-time monitoring.
- Voice-enabled chatbot interactions for improved accessibility.
- Advanced diagnostic features using deep learning.
- Appointment scheduling with healthcare providers.

---

## Contact

- Author: Diwakar Nagaraju
- GitHub: [Diwakar Nagaraju](https://github.com/diwakarnagaraju)
- Email: diwakarnike7@gmail.com



