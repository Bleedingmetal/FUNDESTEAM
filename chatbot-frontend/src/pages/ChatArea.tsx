import { useEffect, useRef } from "react";
import { ChatMessage } from "../components/ChatMessage";
import { WelcomeMessage } from "../components/WelcomeMessage";
import { ScrollArea } from "../components/ui/scroll-area";

export interface Message {
    id: string;
    content: string;
    isUser: boolean;
    timestamp: Date;
}

interface ChatAreaProps {
    messages: Message[];
}

export function ChatArea({ messages }: ChatAreaProps) {
    const scrollAreaRef = useRef<HTMLDivElement>(null);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

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
                <div ref={messagesEndRef} />
            </div>
        </ScrollArea>
    );
}