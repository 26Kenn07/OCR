import streamlit as st
import subprocess
from PIL import Image
import pytesseract

# Function to install Tesseract and its language data
def install_tesseract():
    # Command to install tesseract
    install_tesseract_command = ['brew', 'install', 'tesseract']
    install_lang_command = ['brew', 'install', 'tesseract-lang']

    # Run the command for tesseract
    tesseract_result = subprocess.run(install_tesseract_command, capture_output=True, text=True)
    if tesseract_result.returncode == 0:
        st.success("Tesseract installed successfully.")
    else:
        st.error(f"Error installing Tesseract: {tesseract_result.stderr}")

    # Run the command for tesseract-lang
    lang_result = subprocess.run(install_lang_command, capture_output=True, text=True)
    if lang_result.returncode == 0:
        st.success("Tesseract language data installed successfully.")
    else:
        st.error(f"Error installing Tesseract language data: {lang_result.stderr}")

# Streamlit app layout
st.title("OCR and Keyword Search (Hindi & English)")

# Check and install Tesseract if needed
if st.button("Install Tesseract and Language Data"):
    install_tesseract()

uploaded_image = st.file_uploader("Upload an image (JPEG/PNG)", type=['png', 'jpeg', 'jpg'])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    
    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(img, lang='eng+hin')

    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=300)

    search_term = st.text_input("Enter a keyword to search within the extracted text:")

    if search_term:
        st.subheader("Search Results:")
        if search_term.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_term}' found in the extracted text.")
        else:
            st.write(f"Keyword '{search_term}' not found.")
