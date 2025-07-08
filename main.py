from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create-checkout-session")
async def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "eur",
                        "product_data": {
                            "name": "Finance Flow Premium",
                        },
                        "unit_amount": 1999,
                    },
                    "quantity": 1,
                }
            ],
            success_url="https://crsetsolutions.com/sucesso",
            cancel_url="https://crsetsolutions.com/cancelado",
        )
        return JSONResponse(content={"sessionId": session.id})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
