import os
from typing import IO
from io import BytesIO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY
from .exceptions import TextToSpeechError

class TextToSpeechConverter:
    def __init__(self):
        self.client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    def text_to_speech_stream(self, text: str) -> IO[bytes]:
        try:
            response = self.client.text_to_speech.convert(
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

            audio_stream = BytesIO()
            for chunk in response:
                if chunk:
                    audio_stream.write(chunk)
            audio_stream.seek(0)
            return audio_stream
        except Exception as e:
            raise TextToSpeechError(f"Failed to convert text to speech: {str(e)}")
