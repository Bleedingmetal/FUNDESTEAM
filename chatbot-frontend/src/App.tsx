import { useState, useEffect } from "react";
import { Header } from "./components/Header";
import { ChatArea } from "./components/ChatArea";
import { ChatInput } from "./components/ChatInput";

interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
}

// 
const BACKEND_URL = "http://localhost:8000";

export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isTyping, setIsTyping] = useState(false);

  // Reset backend session on page reload
  useEffect(() => {
    fetch(`${BACKEND_URL}/reset`, { method: "POST" });
  }, []);

  const handleSendMessage = async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      content,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setIsTyping(true);

    try {
      const res = await fetch(`${BACKEND_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: content }),
      });

      const data = await res.json();

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: data.response || "Error: No response from server",
        isUser: false,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: "Error connecting to backend.",
        isUser: false,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="h-screen flex flex-col bg-background">
      <Header />
      <ChatArea messages={messages} isTyping={isTyping} />
      <ChatInput onSendMessage={handleSendMessage} disabled={isTyping} />
    </div>
  );
}
