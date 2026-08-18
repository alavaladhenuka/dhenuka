import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from app.api.endpoints import router as api_router

# 1. Load environment variables from the .env file in backend/
load_dotenv()

# 2. Extract API Key safely from environment
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize Gemini Client with explicit API key fallback
if api_key:
    client = genai.Client(api_key=api_key)
else:
    # Fallback to standard client initialization if environment is pre-configured
    client = genai.Client()

app = FastAPI(
    title="Smart Warehouse AI API",
    description="Automated Warehouse Inventory, Expiry Discounting & Damage Assessment",
    version="1.0.0"
)

# Enable CORS for frontend connection (React running on localhost:5173 or localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Endpoints Router
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "Smart Warehouse AI Backend Service is running."
    }