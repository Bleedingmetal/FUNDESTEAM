import { useEffect, useRef, useState } from "react";
import { ChatMessage } from "./ChatMessage";
import { WelcomeMessage } from "./WelcomeMessage";
import { ScrollArea } from "./ui/scroll-area";

interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
}

interface ChatAreaProps {
  messages: Message[];
  isTyping: boolean;
}

export function ChatArea({ messages, isTyping }: ChatAreaProps) {
  const scrollAreaRef = useRef<HTMLDivElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const [dotCount, setDotCount] = useState(1);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isTyping]);

  useEffect(() => {
    if (!isTyping) {
      setDotCount(1);
      return;
    }

    const interval = setInterval(() => {
      setDotCount((prev) => (prev >= 4 ? 1 : prev + 1));
    }, 500); // change dot every 500ms

    return () => clearInterval(interval);
  }, [isTyping]);

  if (messages.length === 0) {
    return <WelcomeMessage />;
  }

  return (
      <ScrollArea className="flex-1">
        <div ref={scrollAreaRef} className="max-w-4xl mx-auto">
          {messages.map((message) => (
              <ChatMessage
                  key={message.id}
                  message={message.content}
                  isUser={message.isUser}
                  timestamp={message.timestamp}
              />
          ))}

          {isTyping && (
              <div className="flex items-center gap-1 p-2">
                {[...Array(dotCount)].map((_, i) => (
                    <span
                        key={i}
                        className="w-2 h-2 bg-gray-400 rounded-full animate-pulse"
                    />
                ))}
                <span className="ml-2 text-gray-500 italic text-sm">AI is typing...</span>
              </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>
  );
}
