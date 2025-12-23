import React, { useState } from "react";

type BackendResponse = {
    responses: string[]; // either length 1 or 2
};

const App: React.FC = () => {
    const [inputMessage, setInputMessage] = useState("");
    const [serverResponses, setServerResponses] = useState<string[]>([]);
    const [selectedResponse, setSelectedResponse] = useState<string | null>(null);

    // send user message to backend
    const sendMessage = async () => {
        try {
            const response = await fetch("http://localhost:8000/api/message", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: inputMessage }),
            });

            if (!response.ok) {
                console.error("Error:", response.statusText);
                return;
            }

            const data: BackendResponse = await response.json();
            setServerResponses(data.responses);
            setSelectedResponse(null); // reset choice
        } catch (err) {
            console.error("Error sending message:", err);
        }
    };

    // request PDF from backend
    const requestPDF = async () => {
        try {
            const response = await fetch("http://localhost:8000/api/pdf", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ conversation: serverResponses }),
            });

            if (!response.ok) {
                console.error("PDF request failed:", response.statusText);
                return;
            }

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            window.open(url, "_blank");
        } catch (err) {
            console.error("Error fetching PDF:", err);
        }
    };

    return (
        <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
            <h1>Chat with Backend</h1>

            <div>
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    placeholder="Write a message"
                    style={{ width: "60%", marginRight: "1rem" }}
                />
                <button onClick={sendMessage}>Send</button>
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
                                background:
                                    selectedResponse === resp ? "#AAF" : "lightgray",
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

            <button style={{ marginTop: "2rem" }} onClick={requestPDF}>
                📄 Get PDF
            </button>
        </div>
    );
};

export default App;
