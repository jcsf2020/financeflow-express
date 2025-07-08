
#!/usr/bin/env python3
"""
Script para testar os endpoints do backend Stripe
"""
import requests
import json
import sys

def test_endpoints(base_url):
    """Testa todos os endpoints"""
    
    print(f"🧪 Testando endpoints em: {base_url}")
    print("=" * 50)
    
    # 1. Teste Health Check
    print("\n1. Testando /health")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Resposta: {response.json()}")
        else:
            print(f"   ❌ Erro: {response.text}")
    except Exception as e:
        print(f"   ❌ Erro de conexão: {e}")
    
    # 2. Teste Root
    print("\n2. Testando /")
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Resposta: {response.json()}")
        else:
            print(f"   ❌ Erro: {response.text}")
    except Exception as e:
        print(f"   ❌ Erro de conexão: {e}")
    
    # 3. Teste Create Checkout Session
    print("\n3. Testando /create-checkout-session")
    try:
        payload = {
            "product_name": "Teste CRSET - Consultoria Financeira",
            "price_amount": 10000,  # R$ 100,00 em centavos
            "currency": "brl",
            "quantity": 1
        }
        
        response = requests.post(
            f"{base_url}/create-checkout-session",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=15
        )
        
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Sessão criada!")
            print(f"   📝 Session ID: {data.get('session_id')}")
            print(f"   🔗 Checkout URL: {data.get('checkout_url')}")
            return data.get('session_id')
        else:
            print(f"   ❌ Erro: {response.text}")
            return None
    except Exception as e:
        print(f"   ❌ Erro de conexão: {e}")
        return None
    
    # 4. Teste Webhook (simulação)
    print("\n4. Testando /webhook")
    try:
        # Payload de exemplo (evento simulado)
        webhook_payload = {
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "id": "cs_test_example",
                    "payment_status": "paid"
                }
            }
        }
        
        response = requests.post(
            f"{base_url}/webhook",
            json=webhook_payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Webhook processado: {response.json()}")
        else:
            print(f"   ⚠️  Resposta: {response.text}")
    except Exception as e:
        print(f"   ❌ Erro de conexão: {e}")

if __name__ == "__main__":
    # URL do backend
    backend_url = sys.argv[1] if len(sys.argv) > 1 else "https://financeflow-backend-production.up.railway.app"
    test_endpoints(backend_url)
