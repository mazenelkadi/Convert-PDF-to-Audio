import PyPDF2  # Library to work with PDF files
import pyttsx3  # Text-to-speech conversion library
from tkinter.filedialog import *  # GUI dialog box functions from Tkinter
import os  # Provides functions for interacting with the operating system


def save_text_to_audio(text, output_file):
    # Initialize the text-to-speech engine
    speak = pyttsx3.init()
    # Set properties for audio output (optional)
    speak.setProperty("rate", 150)  # Adjust the speaking rate as needed
    # Convert text to speech and save it to a file
    speak.save_to_file(text, output_file)
    # Run the text-to-speech engine
    speak.runAndWait()


# Prompt the user to select a PDF file
book = askopenfilename()

# Check if a file was selected
if book:
    pdfReader = PyPDF2.PdfReader(book)  # Create a PDF reader object

    # Initialize an empty string to store the extracted text
    full_text = ""

    # Extract text from each page and concatenate it
    for page in pdfReader.pages:
        full_text += page.extract_text()

    # Prompt the user to specify the output audio file
    output_file = asksaveasfilename(
        defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    # Check if an output file name was provided
    if output_file:
        # Convert and save the text to audio
        save_text_to_audio(full_text, output_file)
        print(f"Text saved as audio to {output_file}")
    else:
        print("Saving was canceled.")
else:
    print("No PDF file selected.")
