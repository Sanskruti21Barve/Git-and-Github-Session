import requests
import base64

# 1. Use your API key from Google AI Studio
API_KEY = "AIzaSyA441Hpp1L43YCIBGy6f26RYTktOc4SvDI" 

# 2. UPDATED URL: Using gemini-2.5-flash (The stable current version)
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

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
    
    # This will catch any errors and show them in your Streamlit app
    if 'error' in result:
        raise Exception(result['error']['message'])
        
    return result['candidates'][0]['content']['parts'][0]['text']
