import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not TAVILY_API_KEY:
    raise EnvironmentError("Missing TAVILY_API_KEY")

if not GOOGLE_API_KEY:
    raise EnvironmentError("Missing GOOGLE_API_KEY")

if __name__ == "__main__":
    print(f"Config loaded successfully: {TAVILY_API_KEY}")