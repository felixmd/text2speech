import pygame
from typing import IO

class AudioPlayer:
    def play_audio(self, audio_stream: IO[bytes]):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_stream)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
