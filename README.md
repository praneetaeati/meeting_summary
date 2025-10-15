# Meeting Summarizer

A full-stack application that transcribes meeting audio and generates AI-powered summaries with key decisions and action items using Groq AI.

## 🚀 Features

- 🎤 Upload meeting audio files (MP3, WAV, M4A)
- 📝 Automatic transcription (simulated + OpenAI Whisper support)
- 🤖 AI-powered summarization using Groq LLM
- 📊 Structured output: Summary, Key Decisions, Action Items
- 💻 Modern React frontend with Tailwind CSS
- 🐍 FastAPI backend
- ⚡ Real-time processing

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Python web framework
- **Groq API** - LLM for summarization
- **OpenAI Whisper** - Speech-to-text (optional)
- **Python-multipart** - File upload handling

### Frontend
- **React** - Frontend framework
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Groq API account

### Backend Setup
```bash
cd backend
pip install -r requirements.txt

# Create .env file
echo GROQ_API_KEY=your_groq_api_key_here > .env

# Start backend server
uvicorn main:app --reload --port 8000