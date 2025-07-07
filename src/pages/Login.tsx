import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    localStorage.setItem('token', 'fake-token');
    navigate('/');
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '5rem' }}>
      <h2>Login</h2>
      <button onClick={handleLogin}>Entrar</button>
    </div>
  );
};

export default Login;
