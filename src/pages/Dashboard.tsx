const Dashboard = () => {
  const email = "user@crset.com"; // Substituir depois por dado real do JWT, se necessário

  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/login';
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '5rem' }}>
      <h2>Bem-vindo ao Dashboard</h2>
      <p>Autenticado como: {email}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;
