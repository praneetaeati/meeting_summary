import os
from dotenv import load_dotenv

print("Current directory:", os.getcwd())
print("Files in current directory:", os.listdir('.'))

# Load environment variables
load_dotenv()

# Check if .env file exists
env_path = '.env'
if os.path.exists(env_path):
    print(f"✅ .env file found at: {env_path}")
    with open(env_path, 'r') as f:
        content = f.read()
        print(".env content:")
        print(content)
else:
    print(f"❌ .env file NOT found at: {env_path}")

# Check the API key
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    print(f"✅ GROQ_API_KEY found: {api_key[:10]}...")  # Show first 10 chars for security
else:
    print("❌ GROQ_API_KEY not found in environment variables")