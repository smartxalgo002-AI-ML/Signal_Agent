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

    return TavilySearch(
        tavily_api_key=api_key, 
        include_raw_content=True,
        topic="news",           # Focuses on news articles
        time_range="day",       # Filters for results from the last 24 hours
        search_depth="advanced" # Higher quality/more technical results
    )

if __name__ == "__main__":
    try:
        tavily_tool = get_tavily()
        
        print("Searching for the latest tech news...")
        response = tavily_tool.invoke({"query": "What is the date and time IST?"})
        
        # The tool is returning a dictionary with a 'results' list
        if isinstance(response, dict) and "results" in response:
            search_results = response["results"]
            
            for i, result in enumerate(search_results, 1):
                print(f"\n--- Result {i} ---")
                print(f"Title: {result.get('title', 'No Title')}")
                print(f"URL:   {result.get('url', 'No URL')}")
                # Print a snippet of the content
                content = result.get('content', 'No Content')
                print(f"Snippet: {content}")
        else:
            # Fallback in case the structure changes or is a simple string
            print("\nResponse received:")
            print(response)
            
    except Exception as e:
        print(f"An error occurred: {e}")
