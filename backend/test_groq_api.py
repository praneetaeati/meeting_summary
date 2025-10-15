import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_groq():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in .env file")
        return False
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [{"role": "user", "content": "Say 'Hello World'"}],
        "model": "llama-3.1-8b-instant",
        "temperature": 0.3,
        "max_tokens": 10
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Groq API is working!")
            result = response.json()
            print(f"Response: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"❌ Groq API error: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Groq API: {e}")
        return False

if __name__ == "__main__":
    test_groq()