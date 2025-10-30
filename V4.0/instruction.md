brew services start redis
brew services stop redis


let ws = new WebSocket("ws://127.0.0.1:8000/ws/extension/");

ws.onopen = () => {
    console.log("Connected!");
    ws.send("Hello server!");  // ✅ safe to send here
};

ws.onmessage = (e) => {
    console.log("Message:", e.data);
};

daphne myproject.asgi:application --port 8001
python manage.py runserver 127.0.0.1:8001
npm install -g wscat
wscat -c ws://127.0.0.1:8000/ws/extension/
uvicorn Chatbot.asgi:application --host 0.0.0.0 --port 8001

