import { Message } from "../pages/ChatPage";
import ChatMessage from "./ChatMessage";

interface ChatWindowProps {
  messages: Message[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
  return (
    <div className="flex-1 p-4 overflow-y-auto space-y-3">
      {messages.map((msg) => (
        <ChatMessage key={msg.id} message={msg} />
      ))}
    </div>
  );
};

export default ChatWindow;
