# OCR and Keyword Search (Hindi & English)

## Description

This application allows users to upload images in JPEG or PNG format and extract text using Optical Character Recognition (OCR). The extracted text can be searched for specific keywords in both Hindi and English, with the ability to highlight found keywords.

## Features

- Upload images in JPEG or PNG format.
- Extract text from images using Tesseract OCR.
- Search for keywords in the extracted text.
- Highlight found keywords in the displayed text output.

## Requirements

- Python 3.6 or higher
- Streamlit
- Pillow
- Pytesseract
- Tesseract OCR

## Installation

Clone this repository:

   ```
   git clone https://github.com/your-username/ocr-keyword-search.git
   cd ocr-keyword-search
 ```

 
## Create a virtual environment:

    
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

## Install the required packages:

    
    pip install -r requirements.txt
    

## Install Tesseract OCR:

- For Windows: Download the installer from Tesseract at UB Mannheim.

- For macOS: Install via Homebrew:

    ```bash
    brew install tesseract
    ```

    ```bash
    sudo apt-get install tesseract-ocr
    ```

## Usage

- Start the Streamlit server:
    ```bash
    streamlit run app.py
    ```
- Open your web browser and navigate to localhost.

- Upload an image (JPEG or PNG) containing text.

- Enter a keyword to search for in the extracted text.

- View the extracted text and highlighted keywords.



