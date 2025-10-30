import asyncio
import websockets
import json

async def send_message():
    url = "ws://127.0.0.1:8001/ws/extension/BSA"  # your WebSocket URL
    async with websockets.connect(url) as websocket:
        message = {"data": "Hello from Python!"}
        await websocket.send(json.dumps(message))
        print("Message sent:", message)

        # Optional: receive a reply from server
        reply = await websocket.recv()
        print("Reply from server:", reply)

# Run the async function
asyncio.run(send_message())
