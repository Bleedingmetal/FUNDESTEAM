import { Message } from '../pages/ChatPage';

interface ChatMessageProps {
    message: Message;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
    const isUser = message.sender === 'user';
    return (
        <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div
                className={`px-4 py-2 rounded-2xl max-w-xs text-sm shadow-md ${
                    isUser
                        ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-br-none'
                        : 'bg-gradient-to-r from-gray-700 to-gray-800 text-gray-100 rounded-bl-none'
                }`}
            >
                {message.text}
            </div>
        </div>
    );
};

export default ChatMessage;
