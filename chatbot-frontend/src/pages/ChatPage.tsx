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
    const [messages, setMessages] = useState<Message[]>([]);

    const handleSend = (text: string) => {
        if (!text.trim()) return;
        const newMessage: Message = { id: messages.length + 1, text, sender: 'user' };
        setMessages([...messages, newMessage]);

        // Dummy AI response (replace later with backend call)
        setTimeout(() => {
            const aiResponse: Message = {
                id: messages.length + 2,
                text: "This is a placeholder AI response.",
                sender: 'ai',
            };
            setMessages((prev) => [...prev, aiResponse]);
        }, 1200);
    };

    const showWelcome = messages.length === 0;

    return (
        <div className="flex flex-col w-full h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white">
            <ChatHeader />
            <div className="flex-1 flex justify-center items-center">
                <div className="flex flex-col w-full max-w-4xl h-[90%] rounded-2xl shadow-xl border border-gray-700 overflow-hidden bg-gray-900/80 backdrop-blur">
                    {showWelcome ? (
                        <div className="flex-1 flex items-center justify-center">
                            <h2 className="text-3xl font-semibold text-gray-300 text-center">

                            </h2>
                        </div>
                    ) : (
                        <ChatWindow messages={messages} />
                    )}
                    <ChatInput onSend={handleSend} />
                </div>
            </div>
        </div>
    );
};

export default ChatPage;
