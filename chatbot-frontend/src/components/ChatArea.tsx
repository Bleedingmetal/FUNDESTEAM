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
  const [typingMessage, setTypingMessage] = useState("AI is thinking");

  const typingOptions = [
    "AI is thinking",
    "Looking through WRO files",
    "Reading relevant files",
    "Analyzing your input",
    "Synthesizing response",
    "Double-checking facts"
  ];

  // Scroll to bottom when messages or typing changes
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isTyping]);

  // Animate the dots and update typing message
  useEffect(() => {
    if (!isTyping) {
      setDotCount(1);
      setTypingMessage("AI is thinking");
      return;
    }

    const interval = setInterval(() => {
      setDotCount((prev) => (prev >= 4 ? 1 : prev + 1));

      // Change typing message every time dotCount loops
      setTypingMessage((prev) => {
        if (dotCount === 4) {
          const next = typingOptions[Math.floor(Math.random() * typingOptions.length)];
          return next;
        }
        return prev;
      });
    }, 500);

    return () => clearInterval(interval);
  }, [isTyping, dotCount]);

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
              <div className="flex items-center gap-2 p-2">
                {/* Animated dots as circles */}
                <div className="flex gap-1">
                  {[...Array(dotCount)].map((_, i) => (
                      <span
                          key={i}
                          className="w-2 h-2 bg-gray-400 rounded-full animate-pulse"
                      />
                  ))}
                </div>

                {/* Typing message with dynamic dots */}
                <span className="text-gray-500 italic text-sm">
              {typingMessage}{".".repeat(dotCount)}
            </span>
              </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>
  );
}
