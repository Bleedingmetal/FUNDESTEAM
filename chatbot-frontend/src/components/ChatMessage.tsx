import { Avatar, AvatarFallback } from "./ui/avatar";
import { User, Sparkles } from "lucide-react";

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
            <p className="whitespace-pre-wrap">{message}</p>
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
