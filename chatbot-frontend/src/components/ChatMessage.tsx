import { Avatar, AvatarFallback } from "./ui/avatar";
import { User, Sparkles } from "lucide-react";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface ChatMessageProps {
    message: string;
    isUser: boolean;
    timestamp: Date;
}

export function ChatMessage({ message, isUser, timestamp }: ChatMessageProps) {
    return (
        <div className={`flex gap-3 p-4 ${isUser ? 'justify-end' : 'justify-start'}`}>
            {!isUser && (
                <Avatar className="w-8 h-8 flex-shrink-0">
                    <AvatarFallback className="bg-primary">
                        <Sparkles className="w-4 h-4 text-primary-foreground" />
                    </AvatarFallback>
                </Avatar>
            )}

            <div className={`max-w-[70%] ${isUser ? 'order-first' : ''}`}>
                <div
                    className={`rounded-2xl px-4 py-3 ${
                        isUser
                            ? 'bg-primary text-primary-foreground ml-auto'
                            : 'bg-muted text-foreground'
                    }`}
                >
                    <ReactMarkdown
                        children={message}
                        components={{
                            code({ node, inline, className, children, ...props }) {
                                const match = /language-(\w+)/.exec(className || "");
                                return !inline && match ? (
                                    <SyntaxHighlighter
                                        style={oneDark}
                                        language={match[1]}
                                        PreTag="div"
                                        {...props}
                                    >
                                        {String(children).replace(/\n$/, "")}
                                    </SyntaxHighlighter>
                                ) : (
                                    <code className={className} {...props}>
                                        {children}
                                    </code>
                                );
                            },
                        }}
                    />
                </div>
                <div className={`text-xs text-muted-foreground mt-1 ${isUser ? 'text-right' : 'text-left'}`}>
                    {timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </div>
            </div>

            {isUser && (
                <Avatar className="w-8 h-8 flex-shrink-0">
                    <AvatarFallback className="bg-secondary">
                        <User className="w-4 h-4 text-secondary-foreground" />
                    </AvatarFallback>
                </Avatar>
            )}
        </div>
    );
}
