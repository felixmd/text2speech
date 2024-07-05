import os
import pygame
from typing import IO
from io import BytesIO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

from config import ELEVENLABS_API_KEY


client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_stream(text: str) -> IO[bytes]:
    # Perform the text-to-speech conversion
    response = client.text_to_speech.convert(
        voice_id="jBpfuIE2acCO8z3wKNLl",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Create a BytesIO object to hold the audio data in memory
    audio_stream = BytesIO()

    # Write each chunk of audio data to the stream
    for chunk in response:
        if chunk:
            audio_stream.write(chunk)

    # Reset stream position to the beginning
    audio_stream.seek(0)

    # Return the stream for further use
    return audio_stream

def play_audio(audio_stream: IO[bytes]):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio from the BytesIO object
    pygame.mixer.music.load(audio_stream)

    # Play the audio
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Generate and play the audio
audio_stream = text_to_speech_stream("Once upon a time, in a cozy forest, there lived a bunny named Bella and her best friend, Timmy the Turtle. One sunny day, they found a shiny pebble by the pond. They showed it to Oliver the Owl, who told them it was magical and would give sweet dreams if placed under a pillow. That night, Bella put the pebble under her pillow, and she and Timmy dreamt of flying on a fluffy cloud, meeting new friends. They woke up happy and shared their magical dream with everyone. Bella and Timmy lived happily ever after, always exploring and dreaming. Goodnight!")
play_audio(audio_stream)
