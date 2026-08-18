import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from google import genai
except ImportError:  # pragma: no cover
    genai = None

from app.api.endpoints import router as api_router

# 1. Load environment variables from the .env file in backend/
load_dotenv()

# 2. Extract API Key safely from environment
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize Gemini Client only when an API key exists.
# This allows the app to run in local demo mode without the external key.
if api_key and genai is not None:
    try:
        client = genai.Client(api_key=api_key)
    except Exception:
        client = None
else:
    client = None

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