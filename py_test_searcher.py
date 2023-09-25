import webbrowser


def search_defect(querys):
    """Searches for a defect in different search engines.

    Args:
      querys: A list of defects to search for.
    """

    search_engines = {
        "google": "search?q=",
        "bing": "search?q=",
        "yahoo": "search?q=",
        "duckduckgo": "?q=",
        "pinterest": "search?q=",
        "youtube": "results?search_query=",
        "stackoverflow": "search?q=",
        "reddit": "search?q="
    }

    for search_engine, search_param in search_engines.items():
        for query in querys:
            url = f"https://{search_engine}.com/{search_param}{query}"
            webbrowser.open(url)

# Prompt the user for search queries
search_queries = []
print("What would you like to search for today? (Type 'thanks' to exit): ")
while True:
    user_query = input()

    # Check if the user wants to exit
    if user_query.lower() == "thanks":
        break

    # Add the query to the list
    search_queries.append(user_query)

    # Perform the searches
    search_defect(search_queries)

# Print a farewell message
print("Thank you for using the search assistant. Goodbye!")
