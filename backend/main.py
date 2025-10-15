import os
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import aiofiles
from dotenv import load_dotenv

from utils.transcribe import transcribe_audio
from utils.summarize import generate_summary

# Load environment variables
load_dotenv()

app = FastAPI(title="Meeting Summarizer API", version="1.0.0")

# CORS middleware to allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create temporary directory for uploads
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.mp3', '.wav', '.m4a')):
            raise HTTPException(status_code=400, detail="Only MP3, WAV, and M4A files are supported")
        
        # Generate unique filename
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)
        
        # Save uploaded file
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
        
        # Step 1: Transcribe audio
        print("Transcribing audio...")
        transcript = await transcribe_audio(file_path)
        
        if not transcript:
            raise HTTPException(status_code=500, detail="Transcription failed")
        
        # Step 2: Generate summary and action items
        print("Generating summary...")
        summary_data = await generate_summary(transcript)
        
        # Clean up: remove temporary file
        try:
            os.remove(file_path)
        except:
            pass
        
        return JSONResponse({
            "status": "success",
            "filename": file.filename,
            "transcript": transcript,
            "summary": summary_data.get("summary", ""),
            "key_decisions": summary_data.get("key_decisions", []),
            "action_items": summary_data.get("action_items", [])
        })
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Meeting Summarizer API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}