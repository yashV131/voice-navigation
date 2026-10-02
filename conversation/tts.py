import os
from datetime import datetime

import pyttsx3
from playsound3 import playsound


def text_to_speech_from_file(filename):
    # Folder containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Project folder is one level above the script folder
    project_dir = os.path.dirname(script_dir)

    # Input/output directories
    input_text_dir = os.path.join(project_dir, "input", "text")
    output_audio_dir = os.path.join(project_dir, "output", "audio")

    # Create folders if they don't exist
    os.makedirs(input_text_dir, exist_ok=True)
    os.makedirs(output_audio_dir, exist_ok=True)

    # Full path to the input text file
    text_file = os.path.join(input_text_dir, filename)

    # Read text from the file
    with open(text_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Create timestamped output filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(
        output_audio_dir,
        f"tts_{timestamp}.wav"
    )

    # Create speech
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

    # Immediately play the generated audio
    playsound(output_file)

    print(f"Saved TTS audio to: {output_file}")


# Example
text_to_speech_from_file("response.txt")