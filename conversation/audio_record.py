import os
from datetime import datetime

import sounddevice as sd
import soundfile as sf


def record_audio():
    # Folder containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Project folder is one level above the script folder
    project_dir = os.path.dirname(script_dir)

    # Input audio directory
    input_audio_dir = os.path.join(
        project_dir,
        "input",
        "audio"
    )

    # Create folder if it doesn't exist
    os.makedirs(input_audio_dir, exist_ok=True)

    # Create timestamped output filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(
        input_audio_dir,
        f"computer_audio_{timestamp}.wav"
    )

    samplerate = 48000
    channels = 2

    print("Recording...")
    print(f"Saving to: {output_file}")
    print("Press Ctrl+C to stop.")

    try:
        with sf.SoundFile(
            output_file,
            mode="w",
            samplerate=samplerate,
            channels=channels,
            subtype="PCM_16"
        ) as file:

            def callback(indata, frames, time, status):
                if status:
                    print(status)

                file.write(indata)

            with sd.InputStream(
                samplerate=samplerate,
                channels=channels,
                dtype="float32",
                callback=callback
            ):
                while True:
                    sd.sleep(1000)

    except KeyboardInterrupt:
        print("\nRecording stopped.")

    print(f"Saved audio input to: {output_file}")


record_audio()