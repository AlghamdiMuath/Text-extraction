# Text-extraction

Script for extracting text from various document formats, with a focus on PDF files and Arabic content.

## Features

- Extracts text from PDF files
- Focuses on Arabic text extraction but also supports other languages
- Handles multi-page documents
- Processes multiple files in a batch
- Outputs extracted text to easily readable formats

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AlghamdiMuath/Text-extraction.git
   cd Text-extraction
   ```

2. Install the required Python packages:
   pip install pytesseract pdf2image Pillow

## Usage

Run the script from the command line, providing the input and output folder paths:

python pdf_text_extractor.py /path/to/input/folder /path/to/output/folder

Replace /path/to/input/folder with the directory containing your PDF files and /path/to/output/folder with the directory where you want the extracted text files to be saved.
## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
