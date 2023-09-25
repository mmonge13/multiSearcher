import webbrowser

def google_search(query):
    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={query}"

        # Open the default web browser with the search URL
        webbrowser.open(search_url)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
