import React, { useState, useEffect } from 'react';
import { Login } from './components/Login';
import { Register } from './components/Register';
import { Chat } from './components/Chat';
import { api } from './services/api';
import type { User, LoginData, RegisterData } from './types';

type View = 'login' | 'register' | 'chat';

const App: React.FC = () => {
    const [view, setView] = useState<View>('login');
    const [user, setUser] = useState<User | null>(null);
    const [token, setToken] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Check for saved token on mount
    useEffect(() => {
        const savedToken = localStorage.getItem('token');
        const savedUser = localStorage.getItem('user');
        if (savedToken && savedUser) {
            setToken(savedToken);
            setUser(JSON.parse(savedUser));
            setView('chat');
        }
    }, []);

    const handleLogin = async (data: LoginData) => {
        try {
            setLoading(true);
            setError('');
            const response = await api.login(data);
            setToken(response.access_token);
            setUser(response.user);
            localStorage.setItem('token', response.access_token);
            localStorage.setItem('user', JSON.stringify(response.user));
            setView('chat');
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Login failed');
        } finally {
            setLoading(false);
        }
    };

    const handleRegister = async (data: RegisterData) => {
        try {
            setLoading(true);
            setError('');
            const response = await api.register(data);
            setToken(response.access_token);
            setUser(response.user);
            localStorage.setItem('token', response.access_token);
            localStorage.setItem('user', JSON.stringify(response.user));
            setView('chat');
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Registration failed');
        } finally {
            setLoading(false);
        }
    };

    const handleLogout = () => {
        setToken(null);
        setUser(null);
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        setView('login');
    };

    if (loading) {
        return <div style={{ padding: '2rem', textAlign: 'center' }}>Loading...</div>;
    }

    return (
        <div>
            {error && (
                <div style={{
                    padding: '1rem',
                    backgroundColor: '#ff6b6b',
                    color: 'white',
                    textAlign: 'center'
                }}>
                    {error}
                </div>
            )}

            {view === 'login' && (
                <Login
                    onLogin={handleLogin}
                    onSwitchToRegister={() => {
                        setError('');
                        setView('register');
                    }}
                />
            )}

            {view === 'register' && (
                <Register
                    onRegister={handleRegister}
                    onSwitchToLogin={() => {
                        setError('');
                        setView('login');
                    }}
                />
            )}

            {view === 'chat' && user && token && (
                <Chat user={user} token={token} onLogout={handleLogout} />
            )}
        </div>
    );
};

export default App;