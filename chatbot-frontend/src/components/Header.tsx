import { Sparkles } from "lucide-react";

export function Header() {
    return (
        <header className="flex items-center justify-between p-4 border-b border-border bg-background">
            <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-primary rounded-xl flex items-center justify-center">
                    <Sparkles className="w-6 h-6 text-primary-foreground" />
                </div>
                <div className="flex flex-col">
                    <span className="font-medium">AI Coach</span>
                    <span className="text-xs text-muted-foreground">FUNDESTEAM</span>
                </div>
            </div>
            <div className="flex items-center gap-2">
                <span className="text-sm text-muted-foreground">v1.0</span>
            </div>
        </header>
    );
}