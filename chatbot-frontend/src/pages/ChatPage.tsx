import React, { useRef, useState } from "react";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

export interface Message {
  id: number;
  text: string;
  sender: "user" | "ai";
}

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      text: "Hello! I'm your AI assistant. How can I help you today?",
      sender: "ai",
    },
  ]);

  const nextId = useRef(2);
  const [stage, setStage] = useState<"landing" | "chat">("landing");

  const pushMessage = (m: Omit<Message, "id">) =>
    setMessages((prev) => [...prev, { ...m, id: nextId.current++ }]);

  const handleSend = (text: string) => {
    const t = text.trim();
    if (!t) return;

    if (stage === "landing") setStage("chat");
    pushMessage({ sender: "user", text: t });
    setTimeout(() => {
      pushMessage({ sender: "ai", text: "This is a dummy response." });
    }, 1000);
  };

  return (
    <div className="fixed inset-0 bg-[#D6EFFF] flex flex-col overflow-x-hidden overflow-y-hidden">
      {stage === "landing" && (
        <section className="flex-1 w-full flex flex-col items-center justify-center text-center px-4">
          <h1 className="text-4xl md:text-6xl font-semibold text-gray-700 mb-2">
            Hello! I'm your AI assistant.
          </h1>
          <h2 className="text-2xl md:text-4xl font-semibold text-gray-700 mb-8">
            What can I do for you today?
          </h2>

          <div className="w-[min(920px,92%)]">
            <ChatInput onSend={handleSend} started={false} />
          </div>
        </section>
      )}

      {stage === "chat" && (
        <section className="flex-1 w-full flex flex-col">
          <div className="flex-1 min-h-0">
            <ChatWindow messages={messages} />
          </div>

          <div className="px-4 md:px-8 pb-4">
            <div className="mx-auto w-[min(920px,92%)]">
              <ChatInput onSend={handleSend} started={true} />
            </div>
          </div>
        </section>
      )}
    </div>
  );
};

export default ChatPage;
