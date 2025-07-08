
# CRSET Finance Backend - Integração Stripe

Backend FastAPI para integração com Stripe para faturação da CRSET Solutions.

## Endpoints Disponíveis

### 1. Health Check
- **GET** `/health`
- Verifica se o serviço está funcionando

### 2. Criar Sessão de Checkout
- **POST** `/create-checkout-session`
- Cria uma sessão de pagamento no Stripe
- **Body:**
```json
{
  "product_name": "Nome do Produto",
  "price_amount": 10000,
  "currency": "brl",
  "quantity": 1
}
```

### 3. Webhook Stripe
- **POST** `/webhook`
- Recebe eventos do Stripe (pagamentos, falhas, etc.)

### 4. Verificar Sessão
- **GET** `/checkout-session/{session_id}`
- Recupera informações de uma sessão de checkout

### 5. Listar Produtos
- **GET** `/products`
- Lista produtos disponíveis no Stripe

## Configuração

### Variáveis de Ambiente
```bash
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
FRONTEND_URL=https://crsetsolutions.com
PORT=8000
```

### Instalação Local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Docker
```bash
docker build -t crset-backend .
docker run -p 8000:8000 crset-backend
```

## Teste
```bash
python test_endpoints.py https://seu-backend.com
```

## Configuração no Stripe Dashboard

1. **Webhook Endpoint**: Configure `https://seu-backend.com/webhook`
2. **Eventos**: Selecione `checkout.session.completed`, `payment_intent.succeeded`
3. **Secret**: Copie o webhook secret para `STRIPE_WEBHOOK_SECRET`

## Segurança

- Use HTTPS em produção
- Configure webhook secret
- Valide todas as entradas
- Use variáveis de ambiente para chaves sensíveis
