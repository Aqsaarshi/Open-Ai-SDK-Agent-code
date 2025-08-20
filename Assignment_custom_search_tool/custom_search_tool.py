# CUSTOM TOOL TAVILY ASSIGNMENT !!!! 
import requests
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def tavily_search(query: str):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    payload = {
        "query": query,
        "max_results": 5,
        "topic": "general",
        "search_depth": "basic",
        "include_answer": True,
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        answer = data.get("answer", "")
        results = data.get("results", [])
        formatted = "\n".join([f"{r.get('title')} - {r.get('url')}" for r in results])
        return f"Answer:\n{answer}\n\nResults:\n{formatted}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    query = input("Enter your search query: ")
    result = tavily_search(query)
    print("\nSearch Results:\n", result)
