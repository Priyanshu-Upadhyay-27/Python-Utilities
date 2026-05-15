from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from dotenv import load_dotenv

# Load paths from .env file (keeps personal paths out of version control)
load_dotenv()

input_folder = os.getenv('INPUT_FOLDER')
output_folder = os.getenv('OUTPUT_FOLDER')

if not input_folder or not output_folder:
    print("Error: INPUT_FOLDER and OUTPUT_FOLDER must be set in the .env file.")
    print("Copy .env.example to .env and fill in your paths.")
    exit(1)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)
    try:
        if file_name.lower().endswith(('.mp4', '.avi', '.mov')):  # Add formats as needed
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.mp4")  # Set desired output format
            clip = VideoFileClip(input_path)
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")  # Example codec settings
            print(f"Converted {file_name} to {output_path}")
    except Exception as e:
        print(f"Error converting {file_name}: {e}")

