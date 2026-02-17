# from langchain_community.tools.tavily_search import TavilySearchResults

# def get_tavily():
#     return TavilySearchResults()

import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

def get_tavily():
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables.")

    return TavilySearch(tavily_api_key=api_key)
