import { Sparkles, MessageCircle, Lightbulb, Search } from "lucide-react";

export function WelcomeMessage() {
  const suggestions = [
    {
      icon: MessageCircle,
      title: "Start a conversation",
      description: "Ask me anything you'd like to know"
    },
    {
      icon: Lightbulb,
      title: "Get creative help",
      description: "Brainstorm ideas and solutions"
    },
    {
      icon: Search,
      title: "Research topics",
      description: "Explore subjects in depth"
    }
  ];

  return (
    <div className="flex-1 flex items-center justify-center p-8">
      <div className="text-center max-w-2xl">
        <div className="w-16 h-16 bg-gradient-to-br from-primary to-primary/80 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <Sparkles className="w-8 h-8 text-primary-foreground" />
        </div>
        
        <h1 className="text-3xl mb-2">Hello! How can I help you today?</h1>
        <p className="text-muted-foreground mb-8">
          I'm your AI Coach, ready to help with questions, learning, and guidance.
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {suggestions.map((suggestion, index) => (
            <div
              key={index}
              className="p-4 border border-border rounded-xl hover:bg-accent/50 transition-colors cursor-pointer"
            >
              <suggestion.icon className="w-6 h-6 text-primary mb-3 mx-auto" />
              <h3 className="font-medium mb-1">{suggestion.title}</h3>
              <p className="text-sm text-muted-foreground">{suggestion.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}