import os
import speech_recognition

# Get OpenAI API key from environment variable
# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Function to convert client speech into text
def speech_2_text():

    # Obtain audio from the microphone
    speech_recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say something!")
        audio = speech_recognizer.listen(source)

    # Recognize speech using Whisper API
    text = speech_recognizer.recognize_whisper_api(audio)

    try:
        pass
    except speech_recognition.RequestError as exception:
        print("Could not request results from Whisper API")
    return text


speech = speech_2_text()
