import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
import requests
import json

# 1. Configuration (Updated to Gemini 2.5)
API_KEY = os.getenv("GEMINI_API_KEY")
# We changed 'gemini-1.5-flash' to 'gemini-2.5-flash' to fix the 404 error
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def get_summary(employee_data):
    """
    Sends data to the NEW Gemini 2.5 Flash model.
    """
    payload = {
        "contents": [{
            "parts": [{"text": f"Summarize this new hire for HR professionally: {employee_data}"}]
        }]
    }

    try:
        response = requests.post(URL, json=payload)
        result = response.json()
        
        if 'candidates' in result:
            # Returns the text to Member 3
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            # Shows the exact error if one occurs
            error_msg = result.get('error', {}).get('message', 'Unknown AI Error')
            return f"AI Error: {error_msg}"
            
    except Exception as e:
        return f"Connection Error: {e}"

# 2. Test
if __name__ == "__main__":
    print("\n--- CONNECTING TO GEMINI 2.5 ---")
    print(get_summary("Rahul, Sales, rahul@email.com"))
    print("\n--- TEST FINISHED ---")
