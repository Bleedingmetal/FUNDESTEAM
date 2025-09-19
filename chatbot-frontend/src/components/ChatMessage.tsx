import { Message } from "../pages/ChatPage";

interface ChatMessageProps {
  message: Message;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const isUser = message.sender === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        // Text is aligned to the left, and words that are too long can be automatically wrapped.
        // The chat box is up to 60% of the screen length.
        className={`px-5 py-3 rounded-4xl 
                  text-left leading-relaxed break-words whitespace-pre-wrap
                  max-w-[60%]
                ${
                  isUser ? "bg-blue-600 text-white" : "bg-gray-700 text-white"
                }`}
      >
        {message.text}
      </div>
    </div>
  );
};

export default ChatMessage;
