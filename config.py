import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

def get_env_variable(key, default=None):
    value = os.getenv(key, default)
    if value is None:
        value = st.secrets.get(key, default)
    return value

ELEVENLABS_API_KEY = get_env_variable('ELEVENLABS_API_KEY')
