# REPLACE or ADD this code in backend/main.py

from datetime import datetime
from fastapi import FastAPI
from google import genai
from google.genai import types
from pydantic import BaseModel

app = FastAPI()
client = genai.Client()


# Schema forcing AI to return ONLY percentage integer
class DiscountDecision(BaseModel):
    discount_percentage: int
    reasoning: str


@app.post("/calculate-discount")
def calculate_discount(
    manufacture_date: str, expiry_date: str, current_time: str
):
    prompt = f"""
    Analyze the product's shelf life and determine the percentage discount:
    - Manufacturing Date: {manufacture_date}
    - Expiration Date: {expiry_date}
    - Current Date/Time: {current_time}

    Rules:
    1. > 50% remaining shelf life: Return 0% discount.
    2. <= 50% remaining shelf life (more than 0.5 days left): Return 10% or 20% discount.
    3. <= 0.5 days (12 hours) left to expire: Return 50% discount.
    4. Output ONLY percentage integers (0, 10, 20, 50). Do NOT use rupees or currency.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DiscountDecision,
            temperature=0.1,
        ),
    )

    return response.parsed
from fastapi.middleware.cors import CORSMiddleware

# Add this right after creating your app = FastAPI() instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows requests from your Vercel frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)