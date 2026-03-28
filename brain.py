import requests
import base64
import os
from dotenv import load_dotenv

# Load the secret key from your .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Using the stable Gemini 1.5 Flash model
# The specific endpoint for the Robotics preview model
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-1.5-preview:generateContent?key={API_KEY}"
def get_summary(employee_data):
    # This turns the ID image into a format the AI can understand
    image_base64 = base64.b64encode(employee_data.getvalue()).decode("utf-8")
    
    payload = {
        "contents": [{
            "parts": [
                {"text": "Extract Name, Position, and Department from this ID. If not an ID, reply INVALID."},
                {"inline_data": {
                    "mime_type": "image/png", 
                    "data": image_base64
                }}
            ]
        }]
    }
    
    response = requests.post(URL, json=payload)
    result = response.json()
    
    if 'error' in result:
        raise Exception(result['error']['message'])
        
    return result['candidates'][0]['content']['parts'][0]['text']
