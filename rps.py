import redis
import json

def handle_json_signal(message):
    try:
        json_str = message['data'].decode("utf-8")
        data = json.loads(json_str)
        return data
    except Exception as e:
        print("Failed to parse JSON:", e)
        return None

def signal_data(signal):
    try:
        instruments = signal.get("signal", {}).get("instrument", {})
        
        open_price = instruments.get("candle", {}).get("open")
        high_price = instruments.get("candle", {}).get("high")
        low_price = instruments.get("candle", {}).get("low")
        close_price = instruments.get("candle", {}).get("close")
        volume = instruments.get("candle", {}).get("volume")
        trades = instruments.get("candle", {}).get("trades")
        timestamp = instruments.get("candle", {}).get("timestamp")
        
        symbol_name = instruments.get("marketData", {}).get("symbolName")
        
        return {
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price,
            "volume": volume,
            "trades": trades,
            "timestamp": timestamp,
            "symbol_name": symbol_name
        }
    except Exception as e:
        print("Failed to parse JSON:", e)
        return None

def start_subscriber():

    r = redis.Redis(
        host='redis-16697.fcrce171.ap-south-1-1.ec2.cloud.redislabs.com',
        port=16697,
        username='default',
        password='cIPrikVD8KrsU56W5xxyqBVAE1RpJvnT',
        decode_responses=False
    )

    pubsub = r.pubsub()
    channel_name = 'signals.strategy.to_ai'
    pubsub.subscribe(channel_name)

    print(f"Listening for JSON signals on channel: {channel_name}...\n")

    try:
        for message in pubsub.listen():
            if message['type'] == 'message':
                signal = handle_json_signal(message)

                if signal:
                    # ✅ process signal here
                    # print("Received:", signal)
                    data = signal_data(signal)
                    print(data)
                    # return signal

                # 🔁 Loop continues automatically

    except KeyboardInterrupt:
        print("Stopping subscriber...")

    finally:
        pubsub.close()


if __name__ == "__main__":
    signal = start_subscriber()
    print("Received Signal:", signal)