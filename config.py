import os
from dotenv import load_dotenv
from google import genai
from api_key import YOUR_API_KEY

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=YOUR_API_KEY)

# Model name
MODEL = "gemini-2.0-flash"