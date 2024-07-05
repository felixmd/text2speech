class TextToSpeechError(Exception):
    """
    Exception raised for errors in the text-to-speech conversion process.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
