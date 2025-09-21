import { Message } from "../pages/ChatPage";

interface ChatMessageProps {
  message: Message;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const isUser = message.sender === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`px-4 py-2 rounded-2xl max-w-[72%] md:max-w-[60%] leading-6 shadow-sm
                    break-words whitespace-pre-wrap text-left
          ${isUser ? "bg-blue-600 text-white" : "bg-gray-800 text-gray-100"}`}
      >
        {message.text}
      </div>
    </div>
  );
};

export default ChatMessage;


