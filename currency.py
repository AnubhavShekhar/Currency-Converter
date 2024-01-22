from dotenv import load_dotenv
import os
import requests

load_dotenv()

"""
Setting API key
"""

API_TOKEN = os.getenv("API_KEY")
URL = f"{os.getenv("BASE_URL")}{API_TOKEN}"

