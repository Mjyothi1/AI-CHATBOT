from duckduckgo_search import DDGS

def web_search(query):
    try:
        with DDGS() as ddgs:
            results = [r["body"] for r in ddgs.text(query, max_results=3)]
        return "\n".join(results)
    except:
        return "No web results found."
