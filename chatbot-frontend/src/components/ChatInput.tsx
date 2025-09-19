import { useState } from "react";

interface ChatInputProps {
  onSend: (text: string) => void;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSend }) => {
  const [text, setText] = useState("");

  const handleSend = () => {
    onSend(text);
    setText("");
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="p-4 bg-[#EFF6FF]">
      <div className="relative">
        <textarea
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          onInput={(e) => {
            const el = e.currentTarget;
            el.style.height = "auto";
            el.style.height =
              Math.min(el.scrollHeight, window.innerHeight * 0.2) + "px";
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSend();
            }
          }}
          rows={1}
          className="w-[90vh] px-4 py-3 pr-15 border border-gray-600 rounded-2xl 
                      placeholder-gray-500 text-gray-800 [&::-webkit-scrollbar]:hidden
                      focus:outline-none focus:ring-2 
                      focus:ring-blue-500 focus:border-transparent"
          placeholder="Enter Your Question"
        />
        <button
          onClick={handleSend}
          className="absolute bottom-[6.8px] right-104  
                      w-12 h-12 flex items-center justify-center
                      rounded-2xl bg-[#D6EFFF] text-gray-800 ring-2 ring-blue-400
                      hover:bg-blue-500 hover:text-white"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInput;
