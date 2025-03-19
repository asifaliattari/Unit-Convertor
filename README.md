# Unit Converter with Streamlit and Gemini

Unit Converter is a Python-based web application built using Streamlit that allows users to easily convert different units such as temperature, length, and weight. The app also integrates the Gemini chatbot, which provides interactive and intelligent responses to user queries, making the app more user-friendly and dynamic. The chatbot can answer questions related to unit conversion, help with conversions, and engage in general conversation.

## Chatbot Integration with Gemini 3.5

This project also integrates the Gemini 3.5 chatbot, which provides an intelligent conversational experience for users. The chatbot can:

- Answer general questions.
- Assist users with unit conversions.
- Engage in casual conversation to enhance user interaction.

The chatbot is powered by the Gemini 3.5 model and interacts through a user-friendly chat interface built into the Streamlit app.

### How It Works:
- When users open the app, they can use the chat feature to ask questions or receive help with unit conversions.
- The chatbot responds intelligently based on the queries and provides the appropriate assistance.

## Installation (Including Chatbot Integration)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/unit-converter.git

cd unit-converter

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
export GEMINI_API_KEY='your-api-key'
streamlit run app.py

## Example Interactions with Chatbot:
- User: "How do I convert 5 kilometers to miles?"
- Chatbot: "5 kilometers is equal to 3.1 miles."

- User: "What's the weather like today?"
- Chatbot: "I'm not sure about the weather, but I can help you with unit conversions!"

- User: "Can you help me with temperature conversions?"
- Chatbot: "Sure! Just tell me the temperature and the units you'd like to convert."


