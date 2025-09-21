import { useState } from "react";

interface ChatInputProps {
  onSend: (text: string) => void;
  started?: boolean;
}

const ChatInput: React.FC<ChatInputProps> = ({ onSend }) => {
  const [text, setText] = useState("");

  const handleSend = () => {
    const t = text.trim();
    if (!t) return;
    onSend(t);
    setText("");
  };

  return (
    <div className="p-0 bg-transparent">
      <div
        className="relative flex items-stretch border border-gray-500/60 
                      rounded-2xl overflow-hidden bg-white/70 backdrop-blur"
      >
        <textarea
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
          placeholder="Enter Your Question"
          className="w-full flex-1 px-4 py-3 placeholder-gray-500 text-gray-800 
                     focus:outline-none resize-none leading-6
                     [&::-webkit-scrollbar]:hidden"
        />
        <button
          onClick={handleSend}
          className="px-5 min-w-[3.5rem] flex items-center justify-center
                     bg-blue-500 text-white font-medium hover:bg-blue-600
                     transition-colors border-l border-gray-500/60"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInput;
