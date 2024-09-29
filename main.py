import pytesseract
from PIL import Image
import streamlit as st
import re

st.title("OCR and Keyword Search (Hindi & English)")

uploaded_image = st.file_uploader("Upload an image (JPEG/PNG)", type=['png', 'jpeg', 'jpg'])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    
    extracted_text = pytesseract.image_to_string(img, lang='eng+hin')

    st.subheader("Extracted Text:")
    st.text_area("Text", extracted_text)

    search_term = st.text_input("Enter a keyword to search within the extracted text:")

    if search_term:
        st.subheader("Search Results:")
        
        if search_term.lower() in extracted_text.lower():
            st.write(f"Keyword '{search_term}' found in the extracted text.")

            def highlight_keyword(text, keyword):
                highlighted_text = re.sub(f"({re.escape(keyword)})", r'<span style="background-color: yellow; color: black;">\1</span>', text, flags=re.IGNORECASE)
                return highlighted_text
            
            highlighted_text = highlight_keyword(extracted_text, search_term)

            st.markdown(f"<div style='white-space: pre-wrap;'>{highlighted_text}</div>", unsafe_allow_html=True)

        else:
            st.write(f"Keyword '{search_term}' not found.")
