import { Message } from '../pages/ChatPage';

interface ChatMessageProps {
    message: Message;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
    const isUser = message.sender === 'user';

    return (
        <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} w-full`}>
            <div
                className={`px-5 py-3 rounded-2xl max-w-[80%] text-base leading-relaxed ${
                    isUser
                        ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-br-none'
                        : 'bg-gray-700 text-gray-100 rounded-bl-none'
                }`}
            >
                {message.text}
            </div>
        </div>
    );
};

export default ChatMessage;
