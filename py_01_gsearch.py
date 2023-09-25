"""
Módulo webbrowser: Proporciona una interfaz de alto nivel
para abrir páginas web en un navegador web predeterminado.
"""
import webbrowser


def google_search(newquery):
    """
    Abre el navegador web predeterminado con una 
    búsqueda en Google basada en la consulta proporcionada.

    :param query: La cadena de consulta que se utilizará para buscar en Google.
    :type query: str
    """
    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={newquery}"

        # Open the default web browser with the search URL
        webbrowser.open(search_url)

    except ValueError as error:
        print(f"An error occurred: {str(error)}")


# Welcome Message
print("Welcome! I'm your Python search assistant.")

search_queries = []  # List to store search queries

print("What would you like to search for today? (Type 'thank' to exit, or 'done' to perform searches): ")  # pylint: disable=line-too-long
while True:
    # Ask the user what they would like to search for
    user_query = input()

    # Check if the user wants to exit
    if user_query.lower() in ("thank"):
        print("Thank you for using the search assistant. Goodbye!")
        break
    if user_query.lower() == "done":
        if search_queries:
            print("Performing searches...")
            for query in search_queries:
                google_search(query)
            search_queries = []  # Clear the list
        else:
            print("No searches to perform.")
    else:
        # Add the query to the list
        search_queries.append(user_query)
