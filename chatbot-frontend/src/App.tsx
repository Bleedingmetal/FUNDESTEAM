import "./App.css";
import ChatPage from "./pages/ChatPage";

function App() {
  return (
    <div className="fixed inset-0 overflow-x-hidden">
      <div className="h-screen w-screen bg-white text-white flex items-center justify-center">
        <ChatPage />
      </div>
    </div>
  );
}

export default App;
