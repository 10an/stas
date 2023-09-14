from elevenlabs import set_api_key, generate, play
from elevenlabs.api import History


ELEVENLABS_API_KEY = "f8e993eb40a6394b12a8f270a3db7a60"
set_api_key(ELEVENLABS_API_KEY)


def text2speech(assistant_text_response):
    audio = generate(
        text=assistant_text_response,
        voice="Bella",
        model='eleven_monolingual_v1'
    )
    return audio

def output_speech(audio):
    play(audio)
