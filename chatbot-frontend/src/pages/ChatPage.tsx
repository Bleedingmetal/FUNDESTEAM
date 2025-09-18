import { useState } from 'react';
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

        // Dummy AI response I will change this to the flask stuff later but rn this is just gonna be like some stuff
        setTimeout(() => {
            const aiResponse: Message = { id: messages.length + 2, text: "The AI doesnt work rn so heres smth aditya wrote: bye bye ", sender: 'ai' };
            setMessages(prev => [...prev, aiResponse]);
        }, 1000);
    };

    return (
        <div className="flex flex-col w-full max-w-md h-full bg-gray-800 rounded-xl shadow-lg overflow-hidden">
            <ChatWindow messages={messages} />
            <ChatInput onSend={handleSend} />
        </div>
    );
};

export default ChatPage;
