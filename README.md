# Audible Alchemist

Audible Alchemist is a Python module that converts text to speech using the Elevenlabs API. It includes functionality to play the generated audio directly. This module is designed to be flexible and easy to integrate into various applications, including Streamlit deployments.

## Table of Contents

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Testing](#testing)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [License](#license)

## Usage

### Configuration

1. **Elevenlabs API Key**:
   - Obtain your Elevenlabs API key from [Elevenlabs](https://www.elevenlabs.com/).
   - Add the API key to a `.env` file in the root directory of your project:
     ```
     ELEVENLABS_API_KEY=your-elevenlabs-api-key
     ```
   - If deploying to Streamlit, you can also configure the key in Streamlit secrets.

### Running the Application

1. **Modify `app.py`**:
   - The main script to convert text to speech and play the audio is `app.py`. You can modify this file to change the input text or integrate it into your application.
   - Example `app.py`:
     ```python
     from audibleAlchemist import TextToSpeechConverter, AudioPlayer

     def main():
         text = "Hello, world!"
         converter = TextToSpeechConverter()
         audio_stream = converter.text_to_speech_stream(text)
         
         player = AudioPlayer()
         player.play_audio(audio_stream)

     if __name__ == "__main__":
         main()
     ```

2. **Run the Application**:
   ```sh
   python app.py


## Environment Variables

Audible Alchemist uses environment variables to manage configurations securely.

1. **.env File**:
   - Create a `.env` file in the root directory with the following content:
     ```
     ELEVENLABS_API_KEY=your-elevenlabs-api-key
     ```

2. **Streamlit Secrets**:
   - If deploying to Streamlit, configure your secrets in the Streamlit secrets management system.

The module will first attempt to load environment variables from the `.env` file and then fallback to Streamlit secrets if necessary.

## Dependencies

- `python-dotenv`: For loading environment variables from a `.env` file.
- `streamlit`: For managing secrets in a Streamlit deployment.
- `pygame`: For playing audio.
- `unittest`: For running tests.

Install these dependencies using:
```sh
pip install -r requirements.txt
```

### License

```markdown
## License

This project is licensed under the MIT License. 
