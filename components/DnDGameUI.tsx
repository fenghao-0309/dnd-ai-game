import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";

export default function DnDGameUI() {
  const [history, setHistory] = useState([
    {
      role: "system",
      content: "Welcome to the AI-powered D&D adventure! Choose a scenario to begin."
    }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!input.trim()) return;
    const userMessage = { role: "user", content: input };
    setHistory((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    // Simulate API call
    const response = await fetch("/api/game", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input, history })
    });

    const data = await response.json();
    setHistory((prev) => [...prev, { role: "system", content: data.reply }]);
    setLoading(false);
  };

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">🧙 AI Dungeon Master</h1>
      <Card className="h-[60vh] overflow-hidden">
        <CardContent className="p-4 h-full">
          <ScrollArea className="h-full pr-2">
            <div className="space-y-4">
              {history.map((msg, idx) => (
                <div
                  key={idx}
                  className={`p-2 rounded-xl ${msg.role === "user" ? "bg-blue-100 text-right" : "bg-gray-100 text-left"}`}
                >
                  {msg.content}
                </div>
              ))}
              {loading && <div className="text-gray-400">Thinking...</div>}
            </div>
          </ScrollArea>
        </CardContent>
      </Card>
      <div className="flex items-center gap-2 mt-4">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your action..."
          className="flex-1"
          onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
        />
        <Button onClick={handleSubmit} disabled={loading}>
          Send
        </Button>
      </div>
    </div>
  );
}
