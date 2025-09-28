import { Message } from '../pages/ChatArea';
import {ChatMessage} from './ChatMessage';

interface ChatWindowProps {
    messages: Message[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
    return (
        <div className="flex-1 overflow-y-auto px-8 py-6 space-y-6 scrollbar-thin scrollbar-thumb-gray-700 scrollbar-track-transparent">
            {messages.map((msg) => (
                <ChatMessage key={msg.id} message={msg} />
            ))}
        </div>
    );
};

export default ChatWindow;
