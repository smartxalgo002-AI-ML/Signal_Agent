# import asyncio
# from src.agent.trading_signal.signal_parser import parse_signal
# from src.agent.services.decision_engine import make_decision

# async def main():

#     signal = parse_signal(r"src/agent/experiment/signal.txt")
#     print(signal)

#     decision = await make_decision(signal)

#     print("\nFinal Decision:")
#     print(decision.model_dump_json(indent=2))

# if __name__ == "__main__":
#     asyncio.run(main())


import os # python -m main
import asyncio
from src.agent.trading_signal.signal_parser import parse_signal
from src.agent.services.decision_engine import make_decision


SIGNALS_DIR = r"src/agent/experiment/signals"


async def process_signal(file_path: str):
    print(f"\nProcessing: {file_path}")

    signal = parse_signal(file_path)

    decision = await make_decision(signal)

    print("Final Decision:")
    print(decision.model_dump_json(indent=2))
    print("=" * 80)


async def main():

    if not os.path.exists(SIGNALS_DIR):
        print("Signals directory not found.")
        return

    files = [
        f for f in os.listdir(SIGNALS_DIR)
        if f.endswith(".txt")
    ]

    if not files:
        print("No signal files found.")
        return

    # Sequential processing (safe)
    for file_name in files:
        file_path = os.path.join(SIGNALS_DIR, file_name)
        await process_signal(file_path)

    print("\nAll signals processed.")


if __name__ == "__main__":
    asyncio.run(main())
