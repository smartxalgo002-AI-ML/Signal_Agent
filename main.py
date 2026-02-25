# =========================================================================================

# import os # python -m main
# import asyncio
# from src.agent.trading_signal.signal_parser import parse_signal
# from src.agent.services.decision_engine import make_decision


# SIGNALS_DIR = r"src/agent/experiment/signals"


# async def process_signal(file_path: str):
#     print(f"\nProcessing: {file_path}")

#     signal = parse_signal(file_path)

#     decision = await make_decision(signal)

#     print("Final Decision:")
#     print(decision.model_dump_json(indent=2))
#     print("=" * 80)


# async def main():

#     if not os.path.exists(SIGNALS_DIR):
#         print("Signals directory not found.")
#         return

#     files = [
#         f for f in os.listdir(SIGNALS_DIR)
#         if f.endswith(".txt")
#     ]

#     if not files:
#         print("No signal files found.")
#         return

#     # Sequential processing (safe)
#     for file_name in files:
#         file_path = os.path.join(SIGNALS_DIR, file_name)
#         await process_signal(file_path)

#     print("\nAll signals processed.")


# if __name__ == "__main__":
#     asyncio.run(main())

# =========================================================================================================================
# =========================================================================================================================

# import asyncio
# from src.agent.trading_signal.signal_parser import parse_signal
# from src.agent.services.decision_engine import make_decision

# async def main():

#     signal = parse_signal(r"src/agent/experiment/signal.txt")
#     print(f"👍👍👍👍👍{signal}")

#     decision = await make_decision(signal)

#     print("\nFinal Decision:")
#     print(decision.model_dump_json(indent=2))

# if __name__ == "__main__":
#     asyncio.run(main())

# =========================================================================================================================
# =========================================================================================================================

import redis
import json
import asyncio

from src.agent.services.decision_engine import make_decision


def create_redis_connection():
    return redis.Redis(
        host='redis-16697.fcrce171.ap-south-1-1.ec2.cloud.redislabs.com',
        port=16697,
        username='default',
        password='cIPrikVD8KrsU56W5xxyqBVAE1RpJvnT',
        decode_responses=False
    )


async def process_signal(signal: dict):
    print("\n📩 Signal received")

    decision = await make_decision(signal)

    print("\n🎯 Final Decision:")
    print(decision.model_dump_json(indent=2))


async def redis_listener():

    r = create_redis_connection()
    pubsub = r.pubsub()
    channel_name = "signals.strategy.to_ai"

    pubsub.subscribe(channel_name)
    print(f"🚀 Listening on {channel_name}...\n")

    for message in pubsub.listen():
        if message["type"] == "message":
            try:
                json_str = message["data"].decode("utf-8")
                signal = json.loads(json_str)

                await process_signal(signal)

            except Exception as e:
                print("❌ Failed to process signal:", e)


if __name__ == "__main__":
    asyncio.run(redis_listener())