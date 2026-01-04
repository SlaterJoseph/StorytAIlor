import React, { useState } from 'react';
import type { LoginData } from '../types';

interface LoginProps {
    onLogin: (data: LoginData) => void;
    onSwitchToRegister: () => void;
}

export const Login: React.FC<LoginProps> = ({ onLogin, onSwitchToRegister }) => {
    const [formData, setFormData] = useState<LoginData>({
        username: '',
        password: ''
    });

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onLogin(formData);
    };

    return (
        <div style={{ padding: '2rem', maxWidth: '400px', margin: '0 auto' }}>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '1rem' }}>
                    <input
                        type="text"
                        placeholder="Username"
                        value={formData.username}
                        onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                        required
                        style={{ width: '100%', padding: '0.5rem' }}
                    />
                </div>
                <div style={{ marginBottom: '1rem' }}>
                    <input
                        type="password"
                        placeholder="Password"
                        value={formData.password}
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                        required
                        style={{ width: '100%', padding: '0.5rem' }}
                    />
                </div>
                <button type="submit" style={{ width: '100%', marginBottom: '1rem' }}>
                    Login
                </button>
            </form>
            <p>
                Don't have an account?{' '}
                <button onClick={onSwitchToRegister} style={{ background: 'none', border: 'none', color: '#646cff', cursor: 'pointer' }}>
                    Register
                </button>
            </p>
        </div>
    );
};