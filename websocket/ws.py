import asyncio
import websockets
import json
import struct
import ssl

# Your WebSocket URL (example)
WS_URL = "wss://api-feed.dhan.co?version=2&token=eyxxxxx&clientId=100xxxxxxx&authType=2"

async def decode_binary_message(message):
    """
    Convert binary message to readable format.
    Modify this function based on backend binary structure.
    """

    try:
        # If backend sends JSON encoded as binary
        decoded_text = message.decode("utf-8")
        return json.loads(decoded_text)

    except:
        # Example: If structured binary (modify as needed)
        # Example unpacking (adjust according to backend format)
        # symbol_id (int), price (float), quantity (int)
        try:
            symbol_id, price, quantity = struct.unpack('!I f I', message)
            return {
                "symbol_id": symbol_id,
                "price": price,
                "quantity": quantity
            }
        except:
            return {"raw_data": message.hex()}


async def listen():
    ssl_context = ssl.create_default_context()

    while True:  # Auto-reconnect loop
        try:
            print("Connecting to WebSocket...")
            async with websockets.connect(WS_URL, ssl=ssl_context) as websocket:
                print("Connected. Listening for data...")

                while True:
                    message = await websocket.recv()

                    if isinstance(message, bytes):
                        data = await decode_binary_message(message)
                    else:
                        data = message

                    print("Received:", data)

        except Exception as e:
            print("Connection error:", e)
            print("Reconnecting in 5 seconds...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(listen())
