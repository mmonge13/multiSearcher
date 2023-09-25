"""
Módulo webbrowser: Proporciona una interfaz de alto nivel
para abrir páginas web en un navegador web predeterminado.
"""
import webbrowser

operator_sets = {
        "Search Operators": [
            '"" exact',
            '- exclusion',
            '* wildcard',
            'AROUND(n) around'
        ],
        "Date Operators": [
            'yyyy-mm-dd',
            'after: yyyy-mm-dd',
            'before: yyyy-mm-dd',
            'yyyy..yyyy'
        ],
        "Source Operators": [
            'site/search:',
            'ext/filetype:',
            'source:',
            'loc/location:',
            'Blogurl:',
            'Cache:'
        ],
        "Boolean Operators": [
            'and',
            'or'
        ],
        "In Operators": [
            'inurl/allinurl:',
            'intitle/allintitle:',
            'intext/allIntext:',
            'inanchor/allinanchor:'
        ],
        "Utility Operators": [
            'Define',
            'Related',
            'Ip address',
            'x un Y',
            '$ xx .. yy',
            '@',
            'Weather:',
            'Map:',
            'Movie:',
            'Stock:'
        ]
    }

def google_search(query):
    """
    Abre el navegador web predeterminado con una 
    búsqueda en Google basada en la consulta proporcionada.

    :param query: La cadena de consulta que se utilizará para buscar en Google.
    :type query: str
    """
    try:
        # Construct the Google search URL
        search_url = f"https://www.google.com/search?q={query}"

        # Open the default web browser with the search URL
        webbrowser.open(search_url)

    except ValueError as error:
        print(f"An error occurred: {str(error)}")

def get_user_choice(prompt, options):
    while True:
        try:
            print(prompt)
            for index, option in enumerate(options, start=1):
                print(f"{index}. {option}")
            user_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= user_choice <= len(options):
                return user_choice - 1  # Return the index of the selected option           
            print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():

    # Define a dictionary to map operators to their processing functions
    operator_processors = {
        '"" exact': lambda query: f'"{query}"',
        '- exclusion': lambda query: f'-{query}',
        '* wildcard': lambda query: f'*{query}',
        'AROUND(n) around': lambda query: f'AROUND(n){query}',
        'yyyy-mm-dd': lambda query: f'daterange:{query}',
        'after: yyyy-mm-dd': lambda query: f'after:{query}',
        'before: yyyy-mm-dd': lambda query: f'before:{query}',
        'yyyy..yyyy': lambda query: f'daterange:{query}',
        'site/search:': lambda query: f'site:{query}',
        'ext/filetype:': lambda query: f'filetype:{query}',
        'source:': lambda query: f'source:{query}',
        'loc/location:': lambda query: f'location:{query}',
        'Blogurl:': lambda query: f'blogurl:{query}',
        'Cache:': lambda query: f'cache:{query}',
        'and': lambda query: f'{query} AND',
        'or': lambda query: f'{query} OR',
        'inurl/allinurl:': lambda query: f'inurl:{query}',
        'intitle/allintitle:': lambda query: f'intitle:{query}',
        'intext/allIntext:': lambda query: f'intext:{query}',
        'inanchor/allinanchor:': lambda query: f'inanchor:{query}',
        'Define': lambda query: f'define:{query}',
        'Related': lambda query: f'related:{query}',
        'Ip address': lambda query: f'ip:{query}',
        'x un Y': lambda query: f'{query} X {query}',
        '$ xx .. yy': lambda query: f'${query}',
        '@': lambda query: f'@{query}',
        'Weather:': lambda query: f'weather:{query}',
        'Map:': lambda query: f'map:{query}',
        'Movie:': lambda query: f'movie:{query}',
        'Stock:': lambda query: f'stock:{query}',
    }


    # Welcome Message
    print("Welcome! I'm your Python search assistant.")
    print("Here you can search using operators that are special symbols and commands that can be added to a Google search query to refine and customize your search results") # pylint: disable=line-too-long

    while True:
        # Present the available sets of operators to the user
        operator_set_choices = list(operator_sets.keys())
        selected_set_index = get_user_choice("Choose an operator set:", operator_set_choices)
        selected_set = operator_set_choices[selected_set_index]

        # Initialize an empty list to store query elements
        query_elements = []

    # Welcome Message
        print("Welcome! I'm your Python search assistant.")
        print("Here you can search using operators that are special symbols and commands that can be added to a Google search query to refine and customize your search results") # pylint: disable=line-too-long

        while True:
            # Present the available sets of operators to the user
            operator_set_choices = list(operator_sets.keys())
            selected_set_index = get_user_choice("Choose an operator set:", operator_set_choices)
            selected_set = operator_set_choices[selected_set_index]

            # Initialize an empty list to store query elements
            query_elements = []

            while True:
                # Present the operators in the selected set
                selected_operator_index = get_user_choice(f"{selected_set}:", operator_sets[selected_set] + ["Finish"])
                selected_operator = operator_sets[selected_set][selected_operator_index]

                if selected_operator == "Finish":
                    break

                # Ask the user to enter a search element
                search_element = input("Enter a search element: ")
                query_elements.append(operator_processors[selected_operator](search_element))

            # Combine the elements into a single query
            combined_query = " ".join(query_elements)

            # Perform the Google search
            google_search(combined_query)

            # Ask if the user wants to choose another operator set or continue entering search elements
            another_set = input("\nDo you want to choose another operator set? (yes/no): ")
            if another_set.lower() != 'yes':
                break

if __name__ == "__main__":
    # Welcome Message
    print("Welcome! I'm your Python search assistant.")
    print("Here you can search using operators that are special symbols and commands that can be added to a Google search query to refine and customize your search results") # pylint: disable=line-too-long
    
    main()