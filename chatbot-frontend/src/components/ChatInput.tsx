import { useState } from 'react';

interface ChatInputProps {
    onSend: (text: string) => void;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSend }) => {
    const [text, setText] = useState('');

    const handleSend = () => {
        onSend(text);
        setText('');
    };

    const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') handleSend();
    };

    return (
        <div className="p-4 bg-gray-700 flex gap-2">
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                onKeyDown={handleKeyPress}
                className="flex-1 px-4 py-2 rounded-lg bg-gray-600 text-white focus:outline-none"
                placeholder="Type your message..."
            />
            <button
                onClick={handleSend}
                className="px-4 py-2 bg-blue-600 rounded-lg hover:bg-blue-500 transition"
            >
                Send
            </button>
        </div>
    );
};

export default ChatInput;
