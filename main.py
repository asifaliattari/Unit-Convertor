import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv(override=True)
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: GOOGLE_API_KEY is missing. Set it in the .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Conversion data
conversions = {
    "length": {"meter": 1, "kilometer": 0.001, "mile": 0.000621371, "yard": 1.09361},
    "weight": {"gram": 1, "kilogram": 0.001, "pound": 0.00220462, "ounce": 0.035274},
    "temperature": lambda v, f, t: v * 1.8 + 32 if f == "celsius" and t == "fahrenheit" else (v - 32) / 1.8 if f == "fahrenheit" and t == "celsius" else v,
    "area": {
        "square_feet": 1, "square_yard": 1/9, "marla": 1/272.25, "kanal": 1/5445, "acre": 1/43560, "murabba": 1/1089000, "hectare": 1/107639
    },
    "volume": {"liter": 1, "milliliter": 1000, "cubic_meter": 0.001, "gallon": 0.264172},
    "digital": {"bit": 1, "byte": 1/8, "kilobyte": 1/8000, "megabyte": 1/8e+6, "gigabyte": 1/8e+9}
}

# Streamlit UI
st.title("Unit Converter ( Yard/Sqr feet/Marla, etc.) with Ai")

category = st.selectbox("Select Category", list(conversions.keys()))
from_unit = st.selectbox("From Unit", list(conversions[category]) if category != "temperature" else ["celsius", "fahrenheit"])
to_unit = st.selectbox("To Unit", list(conversions[category]) if category != "temperature" else ["celsius", "fahrenheit"])
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

# Gemini API Handler
def handle_conversion(query):
    try:
        response = model.generate_content(query)
        return response.candidates[0].content.parts[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Local Conversion
def convert_locally(value, from_unit, to_unit):
    if category == "temperature":
        return conversions[category](value, from_unit, to_unit)
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

if st.button("Convert with Detail"):
    query = f"Convert {value} {from_unit} to {to_unit}."
    result = handle_conversion(query)
    st.success(result)

if st.button("Convert Direct"):
    try:
        result = convert_locally(value, from_unit, to_unit)
        st.success(f"Converted Value: {result} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")

# Chatbot Section
st.subheader("Chatbot")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something... (e.g., 'Informations are limited...')", key="chat_input")

def send_message():
    if user_input:
        response = handle_conversion(user_input)
        # Append both user input and bot response to the chat history
        st.session_state.chat_history.append(f"**You:** {user_input}")
        st.session_state.chat_history.append(f"**Bot:** {response}")
        # Clear the input after sending
        st.session_state.chat_input = ""

# Display chat history
if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        st.write(message)

# Send button
st.button("Send", on_click=send_message)
