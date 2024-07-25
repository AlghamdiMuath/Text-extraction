import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import argparse

def extract_text_from_pdf(pdf_path, output_folder):
     
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)
    
    # Create a text file to store the extracted text
    output_file = os.path.join(output_folder, f"{base_name}.txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, image in enumerate(images):
            # Perform OCR on the image
            text = pytesseract.image_to_string(image, lang='ara+eng')
            
            # Write the extracted text to the file
            f.write(f"--- Page {i+1} ---\n")
            f.write(text + "\n\n")
    
    print(f"Text extracted from {pdf_path} and saved to {output_file}")

def main(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process all PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            extract_text_from_pdf(pdf_path, output_folder)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract text from PDF files.")
    parser.add_argument("input_folder", help="Path to the folder containing PDF files")
    parser.add_argument("output_folder", help="Path to the folder where text files will be saved")
    args = parser.parse_args()

    # Run the main function with provided arguments
    main(args.input_folder, args.output_folder)
