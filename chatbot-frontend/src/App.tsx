import { useState } from "react";
import { Header } from "./components/Header";
import { ChatArea } from "./components/ChatArea";
import { ChatInput } from "./components/ChatInput";

interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
}

// Mock AI responses for demonstration
const getAIResponse = (userMessage: string): string => {
  const responses = [
    "I understand you're asking about that. Let me help you with some information and insights.",
    "That's an interesting question! Here are a few thoughts on the topic.",
    "I'd be happy to assist you with that. Here's what I can tell you.",
    "Great question! Based on what you're asking, here's my response.",
    "I can help you with that. Let me provide some relevant information."
  ];
  
  return responses[Math.floor(Math.random() * responses.length)] + 
    ` You mentioned: "${userMessage}". I'm here to help with any follow-up questions you might have.`;
};

export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isTyping, setIsTyping] = useState(false);

  const handleSendMessage = async (content: string) => {
    const userMessage: Message = {
      id: Date.now().toString(),
      content,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsTyping(true);

    // Simulate AI thinking time
    setTimeout(() => {
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: getAIResponse(content),
        isUser: false,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, aiMessage]);
      setIsTyping(false);
    }, 1000 + Math.random() * 2000); // 1-3 seconds delay
  };

  return (
    <div className="h-screen flex flex-col bg-background">
      <Header />
      <ChatArea messages={messages} />
      <ChatInput onSendMessage={handleSendMessage} disabled={isTyping} />
    </div>
  );
}