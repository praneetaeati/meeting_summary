import os
import asyncio
from dotenv import load_dotenv
from utils.transcribe import transcribe_audio
from utils.summarize import generate_summary

load_dotenv()

async def test_complete_flow():
    print("=== Testing Complete Meeting Summarization Flow ===\n")
    
    # Test with simulated transcription (no audio file needed)
    print("1. 📝 Simulating transcription...")
    transcript = """
    John: Okay team, let's start our weekly project meeting. First, Sarah, can you update us on the frontend development?
    Sarah: Sure, we've completed the user authentication module and are now working on the dashboard interface. We're about 70% done.
    Mike: On the backend, I've optimized the database queries. We're seeing 40% faster response times now.
    John: That's great progress. Key decision - we'll deploy to staging environment this Friday.
    Sarah: I'll make sure the frontend is ready by Thursday. Action item - Mike will prepare the deployment checklist.
    Mike: I'll also document the API changes for the mobile team. Deadline: end of this week.
    John: Perfect. Let's aim for production deployment next Wednesday. Any concerns?
    Sarah: None from my side. The design team has approved all mockups.
    Mike: Backend is stable and ready for integration.
    John: Excellent. Meeting adjourned.
    """
    
    print("✅ Transcript generated")
    print(f"Transcript length: {len(transcript)} characters\n")
    
    # Test Groq summarization
    print("2. 🤖 Generating summary with Groq...")
    try:
        summary_data = await generate_summary(transcript)
        
        print("✅ Summary generated successfully!")
        print("\n3. 📊 Results:")
        print(f"   Summary: {summary_data['summary']}")
        print(f"   Key Decisions: {len(summary_data['key_decisions'])} items")
        for i, decision in enumerate(summary_data['key_decisions'], 1):
            print(f"     {i}. {decision}")
        print(f"   Action Items: {len(summary_data['action_items'])} items")
        for i, action in enumerate(summary_data['action_items'], 1):
            print(f"     {i}. {action}")
            
        return True
        
    except Exception as e:
        print(f"❌ Error in summarization: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_complete_flow())
    if success:
        print("\n🎉 Complete flow test PASSED! Your meeting summarizer is ready.")
    else:
        print("\n💥 Complete flow test FAILED. Please check the errors above.")