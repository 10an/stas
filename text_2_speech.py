from elevenlabs import set_api_key, generate, play
from elevenlabs.api import History


def text2speech(api_key, text, voice, model):
    set_api_key(api_key)
    audio = generate(
        text=text,
        voice=voice,
        model=model
    )
    return audio

def output_speech(audio):
    play(audio)
