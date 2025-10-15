import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

async def generate_summary(transcript: str) -> dict:
    """
    Generate meeting summary using Groq API via direct requests
    """
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not groq_api_key:
            raise Exception("GROQ_API_KEY not found in environment variables. Please add it to your .env file")
        
        prompt = f"""
        You are a professional meeting summarizer assistant. Analyze this meeting transcript and provide a structured summary in JSON format.

        Please extract:
        1. A concise summary paragraph (2-3 sentences)
        2. Key decisions made during the meeting (as bullet points)
        3. Action items with assigned owners and deadlines if mentioned (as bullet points)

        Format your response as a JSON object with these exact keys:
        - "summary" (string)
        - "key_decisions" (array of strings)
        - "action_items" (array of strings)

        Transcript:
        {transcript}

        Respond with ONLY the JSON object, no additional text or explanation.
        """
        
        headers = {
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": "llama-3.1-8b-instant",  # ✅ Updated to available model
            "temperature": 0.3,
            "max_tokens": 4000,
            "stream": False
        }
        
        print("Sending request to Groq API...")
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code != 200:
            error_msg = f"Groq API error: {response.status_code} - {response.text}"
            print(error_msg)
            raise Exception(error_msg)
        
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        print("Received response from Groq API")
        
        # Clean the response - remove any markdown code blocks
        content = content.replace('```json', '').replace('```', '').strip()
        
        # Parse the JSON response
        try:
            summary_data = json.loads(content)
            print("Successfully parsed JSON response")
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Raw response: {content}")
            # If JSON parsing fails, create a fallback structure
            summary_data = {
                "summary": "Unable to parse the meeting summary. Please check the transcript.",
                "key_decisions": ["Review the meeting notes for key decisions"],
                "action_items": ["Review the meeting notes for action items"]
            }
        
        return summary_data
        
    except Exception as e:
        print(f"Summary generation error: {str(e)}")
        # Return fallback data with actual transcript content
        return {
            "summary": f"Meeting discussion covered: {transcript[:200]}...",
            "key_decisions": ["Check meeting notes for key decisions"],
            "action_items": ["Review action items from meeting notes"]
        }