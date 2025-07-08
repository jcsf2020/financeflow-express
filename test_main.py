from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import logging
from typing import Optional
import uuid
import time

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="CRSET Finance Backend - TEST MODE",
    description="Backend para integração Stripe - MODO TESTE",
    version="1.0.0-test"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crsetsolutions.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos
class CheckoutSessionRequest(BaseModel):
    product_name: str
    price_amount: int
    currency: str = "brl"
    quantity: int = 1
    success_url: Optional[str] = None
    cancel_url: Optional[str] = None

class CheckoutSessionResponse(BaseModel):
    checkout_url: str
    session_id: str

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "CRSET Finance Backend - TEST MODE",
        "stripe_configured": True,
        "mode": "test",
        "version": "1.0.0-test"
    }

@app.post("/create-checkout-session", response_model=CheckoutSessionResponse)
async def create_checkout_session(request: CheckoutSessionRequest):
    try:
        # Simular criação de sessão
        session_id = f"cs_test_{uuid.uuid4().hex[:24]}"
        checkout_url = f"https://checkout.stripe.com/pay/{session_id}"
        
        logger.info(f"Sessão de teste criada: {session_id}")
        logger.info(f"Produto: {request.product_name}, Valor: R$ {request.price_amount/100:.2f}")
        
        return CheckoutSessionResponse(
            checkout_url=checkout_url,
            session_id=session_id
        )
        
    except Exception as e:
        logger.error(f"Erro: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")

@app.post("/webhook")
async def stripe_webhook(request: Request):
    try:
        payload = await request.body()
        logger.info("Webhook recebido (modo teste)")
        
        # Simular processamento
        return {"status": "success", "mode": "test"}
        
    except Exception as e:
        logger.error(f"Erro no webhook: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")

@app.get("/checkout-session/{session_id}")
async def get_checkout_session(session_id: str):
    return {
        "session_id": session_id,
        "payment_status": "paid",
        "customer_email": "test@example.com",
        "amount_total": 10000,
        "currency": "brl",
        "metadata": {"mode": "test"}
    }

@app.get("/products")
async def list_products():
    return {
        "products": [
            {
                "id": "prod_test_1",
                "name": "Consultoria Financeira CRSET",
                "description": "Serviço de consultoria financeira personalizada",
                "active": True
            },
            {
                "id": "prod_test_2", 
                "name": "Análise de Investimentos",
                "description": "Análise completa de portfólio de investimentos",
                "active": True
            }
        ],
        "mode": "test"
    }

@app.get("/")
async def root():
    return {
        "message": "CRSET Finance Backend API - TEST MODE",
        "version": "1.0.0-test",
        "mode": "test",
        "endpoints": {
            "health": "/health",
            "create_checkout": "/create-checkout-session",
            "webhook": "/webhook",
            "docs": "/docs"
        }
    }
