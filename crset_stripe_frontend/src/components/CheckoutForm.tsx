import { loadStripe } from '@stripe/stripe-js';
import { Elements, useStripe, useElements, CardElement } from '@stripe/react-stripe-js';
import { useState } from 'react';

// Chave pública real inserida abaixo
const stripePromise = loadStripe('pk_live_51BrHDKVB6YrbgeXfVtc1l9d1HX2E5DAp72TQYxSrgHMWcRknr2v34wNMkC81s08VDGkDF0jFCi52FkMQVL83LkH00ekwuCV75');

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!stripe || !elements) return;

    setLoading(true);

    const res = await fetch('http://localhost:8000/create-checkout-session', {
      method: 'POST',
    });

    const { sessionId } = await res.json();

    const result = await stripe.redirectToCheckout({ sessionId });

    if (result.error) alert(result.error.message);

    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit}>
      <CardElement />
      <button type="submit" disabled={!stripe || loading}>
        {loading ? 'A processar...' : 'Pagar agora'}
      </button>
    </form>
  );
};

const StripeWrapper = () => (
  <Elements stripe={stripePromise}>
    <CheckoutForm />
  </Elements>
);

export default StripeWrapper;
