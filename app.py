from audibleAlchemist import TextToSpeechConverter, AudioPlayer

def main():
    text = "Hello, world!"
    converter = TextToSpeechConverter()
    audio_stream = converter.text_to_speech_stream(text)
    
    player = AudioPlayer()
    player.play_audio(audio_stream)

if __name__ == "__main__":
    main()
