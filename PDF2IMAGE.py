from pdf2image import convert_from_path
import os
from dotenv import load_dotenv

# Load paths from .env file (keeps personal paths out of version control)
load_dotenv()

pdf_path = os.getenv('PDF_PATH')
output_folder = os.getenv('OUTPUT_FOLDER', '.')  # defaults to current directory

if not pdf_path:
    print("Error: PDF_PATH must be set in the .env file.")
    print("Copy .env.example to .env and fill in your paths.")
    exit(1)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Convert PDF to a list of images
images = convert_from_path(pdf_path, dpi=300)  # You can change the DPI for better quality

# Save images as JPG
for i, image in enumerate(images):
    output_path = os.path.join(output_folder, f'page_{i + 1}.jpg')
    image.save(output_path, 'JPEG')
    print(f"Saved page {i + 1} to {output_path}")
