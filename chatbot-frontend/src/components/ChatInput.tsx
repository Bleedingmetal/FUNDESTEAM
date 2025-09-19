import { useState } from 'react';

interface ChatInputProps {
    onSend: (text: string) => void;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSend }) => {
    const [text, setText] = useState('');

    const handleSend = () => {
        if (!text.trim()) return;
        onSend(text);
        setText('');
    };

    const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') handleSend();
    };

    return (
        <div className="p-4 bg-gray-900 border-t border-gray-700">
            <div className="flex items-center gap-2">
                <input
                    type="text"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    onKeyDown={handleKeyPress}
                    className="flex-1 px-4 py-3 rounded-xl bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Type your message..."
                />
                <button
                    onClick={handleSend}
                    className="px-5 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-xl hover:opacity-90 transition"
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default ChatInput;
