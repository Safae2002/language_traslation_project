import streamlit as st
from google.cloud import translate_v2 as translate
import os

# Set the path to your credentials file
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = r"____.json" # change it to the JSON file that you get from the Google Translate API

# Initialize translation client
translate_client = translate.Client()

# Streamlit UI
st.set_page_config(page_title="My Translation Tool", page_icon="🌐", layout="wide")
st.title("My Translation Tool")

# Set background and layout styles
st.markdown(
    """
    <style>
    .reportview-container {
        background: #09ece0;  
    }
    .header {
        text-align: center;
        color: #343a40;  
    }
    
    
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)  # Two columns for input and output

with col1:
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    st.subheader("Input Text")
    source_text = st.text_area("Enter text to translate:", height=200)
    target_language = st.selectbox("Select target language:", ["fr", "es", "de", "ar", "zh"])

    if st.button("Translate", key="translate_button"):
        if source_text:
            result = translate_client.translate(source_text, target_language=target_language)
            translated_text = result['translatedText']
        else:
            st.error("Please enter text to translate.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='output-container'>", unsafe_allow_html=True)
    st.subheader("Translated Text")
    # Create a read-only text area to display the translated text
    if 'translated_text' in locals():
        st.text_area("Output", value=translated_text, height=200, disabled=True)
    else:
        st.text_area("Output", value="The translated text will appear here after translation.", height=200,
                     disabled=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Optional: Add footer or additional information
st.markdown("---")
st.write("### About this tool")
st.write(
    "This tool uses Google Cloud Translation API to translate text from one language to another. Enter the text you want to translate, select the target language, and click 'Translate'.")
