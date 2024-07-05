import unittest
import sys
import os
from io import BytesIO

# Adjust the path to include the parent directory of audibleAlchemist
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from audibleAlchemist import TextToSpeechConverter

class TestTextToSpeechConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TextToSpeechConverter()
    
    def test_text_to_speech_stream(self):
        text = "Test"
        audio_stream = self.converter.text_to_speech_stream(text)
        self.assertIsInstance(audio_stream, BytesIO)
        self.assertGreater(len(audio_stream.read()), 0)

if __name__ == "__main__":
    unittest.main()
