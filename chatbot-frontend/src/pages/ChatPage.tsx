import { useState } from 'react';
import ChatHeader from '../components/ChatHeader';
import ChatWindow from '../components/ChatWindow';
import ChatInput from '../components/ChatInput';

/* pls dont mess with this file it took me forever to get all the errors out of here I will NOT hesitate to end you if this breaks*/
export interface Message {
    id: number;
    text: string;
    sender: 'user' | 'ai';
}

const ChatPage = () => {
    const [messages, setMessages] = useState<Message[]>([
        { id: 1, text: "Hello! I'm your AI assistant. How can I help you today?", sender: 'ai' },
    ]);

    const handleSend = (text: string) => {
        if (!text.trim()) return;
        const newMessage: Message = { id: messages.length + 1, text, sender: 'user' };
        setMessages([...messages, newMessage]);

        // Dummy AI response (replace with Flask later)
        setTimeout(() => {
            const aiResponse: Message = {
                id: messages.length + 2,
                text: "The AI doesn’t work rn so here’s smth Aditya wrote: bye bye ",
                sender: 'ai',
            };
            setMessages((prev) => [...prev, aiResponse]);
        }, 1000);
    };

    return (
        <div className="flex flex-col w-full h-screen bg-gray-900 text-white">
            <ChatHeader />
            <div className="flex-1 flex justify-center">
                <div className="flex flex-col w-full max-w-3xl border-x border-gray-700">
                    <ChatWindow messages={messages} />
                    <ChatInput onSend={handleSend} />
                </div>
            </div>
        </div>
    );
};

export default ChatPage;
