import { useEffect, useRef } from "react";
import { ChatMessage } from "./ChatMessage";
import { WelcomeMessage } from "./WelcomeMessage";
import { ScrollArea } from "./ui/scroll-area";
import { motion, AnimatePresence } from "framer-motion";

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

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isTyping]);

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
                <AnimatePresence>
                  {[0, 1, 2, 3].map((i) => (
                      <motion.span
                          key={i}
                          className="w-2 h-2 bg-gray-400 rounded-full"
                          initial={{ opacity: 0 }}
                          animate={{ opacity: [0, 1, 0] }}
                          transition={{
                            repeat: Infinity,
                            duration: 1,
                            repeatDelay: 0,
                            delay: i * 0.2,
                          }}
                      />
                  ))}
                </AnimatePresence>
                <span className="ml-2 text-gray-500 italic text-sm">
              AI is typing...
            </span>
              </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>
  );
}
