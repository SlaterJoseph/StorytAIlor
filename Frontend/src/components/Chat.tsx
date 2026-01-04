import React, { useState } from 'react';
import { api } from '../services/api';
import type { User } from '../types';

interface ChatProps {
    user: User;
    token: string;
    onLogout: () => void;
}

export const Chat: React.FC<ChatProps> = ({ user, token, onLogout }) => {
    const [inputMessage, setInputMessage] = useState("");
    const [serverResponses, setServerResponses] = useState<string[]>([]);
    const [selectedResponse, setSelectedResponse] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {
        try {
            setLoading(true);
            const data = await api.sendMessage(inputMessage, token);
            setServerResponses(data.responses);
            setSelectedResponse(null);
            setInputMessage('');
        } catch (err) {
            console.error("Error sending message:", err);
            alert('Failed to send message');
        } finally {
            setLoading(false);
        }
    };

    const requestPDF = async () => {
        try {
            const blob = await api.getPDF(serverResponses, token);
            const url = URL.createObjectURL(blob);
            window.open(url, "_blank");
        } catch (err) {
            console.error("Error fetching PDF:", err);
            alert('Failed to generate PDF');
        }
    };

    return (
        <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
    <h1>Chat with Backend</h1>
    <div>
    <span style={{ marginRight: '1rem' }}>Welcome, {user.username}!</span>
    <button onClick={onLogout}>Logout</button>
    </div>
    </div>

    <div>
    <input
        type="text"
    value={inputMessage}
    onChange={(e) => setInputMessage(e.target.value)}
    placeholder="Write a message"
    style={{ width: "60%", marginRight: "1rem" }}
    disabled={loading}
    />
    <button onClick={sendMessage} disabled={loading || !inputMessage.trim()}>
    {loading ? 'Sending...' : 'Send'}
    </button>
    </div>

    {serverResponses.length > 0 && (
        <div style={{ marginTop: "1rem" }}>
        <h2>Responses</h2>
        {serverResponses.map((resp, index) => (
            <button
                key={index}
            onClick={() => setSelectedResponse(resp)}
            style={{
            display: "block",
                margin: "0.5rem 0",
                background: selectedResponse === resp ? "#AAF" : "lightgray",
        }}
        >
            {resp}
            </button>
        ))}
        </div>
    )}

    {selectedResponse && (
        <div style={{ marginTop: "1rem" }}>
        <p>Selected: {selectedResponse}</p>
    </div>
    )}

    <button
        style={{ marginTop: "2rem" }}
    onClick={requestPDF}
    disabled={serverResponses.length === 0}
        >
                📄 Get PDF
    </button>
    </div>
);
};