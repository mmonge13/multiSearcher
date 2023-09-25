"""
Módulo webbrowser: Proporciona una interfaz de alto nivel
para abrir páginas web en un navegador web predeterminado.
"""
import webbrowser

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

# Define the sets of search operators
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
        '$ xx..yy',
        '@',
        'Weather:',
        'Map:',
        'Movie:',
        'Stock:'
    ]
}

# Define a dictionary to map operators to their processing functions
operator_processors = {
    '"" exact': lambda query: f'"{query}"',
    '- exclusion': lambda query: f'-{query}',
    '* wildcard': lambda query: f'*{query}',
    'AROUND(n) around': lambda query1, query2: f'{query1}AROUND(n){query2}',
    'yyyy-mm-dd': lambda query: f'daterange:{query}',
    'after: yyyy-mm-dd': lambda query: f'after:{query}',
    'before: yyyy-mm-dd': lambda query: f'before:{query}',
    'yyyy..yyyy': lambda query1, query2: f'daterange:{query1}-{query2}',
    'site/search:': lambda query: f'site:{query}',
    'ext/filetype:': lambda query: f'filetype:{query}',
    'source:': lambda query: f'source:{query}',
    'loc/location:': lambda query: f'location:{query}',
    'Blogurl:': lambda query: f'blogurl:{query}',
    'Cache:': lambda query: f'cache:{query}',
    'and': lambda query1, query2: f'{query1} AND {query2}',
    'or': lambda query1, query2: f'{query1} OR {query2}',
    'inurl/allinurl:': lambda query: f'inurl:{query}',
    'intitle/allintitle:': lambda query: f'intitle:{query}',
    'intext/allIntext:': lambda query: f'intext:{query}',
    'inanchor/allinanchor:': lambda query: f'inanchor:{query}',
    'Define': lambda query: f'define:{query}',
    'Related': lambda query: f'related:{query}',
    'Ip address': lambda query: f'ip:{query}',
    '$ xx..yy': lambda query1, query2: f'${query1}..{query2}',
    '@': lambda query: f'@{query}',
    'Weather:': lambda query: f'weather:{query}',
    'Map:': lambda query: f'map:{query}',
    'Movie:': lambda query: f'movie:{query}',
    'Stock:': lambda query: f'stock:{query}',
}

operators_requiring_two_queries = [
    '"" exact',
    'AROUND(n) around',
    'yyyy..yyyy',
    'and',
    'or',
    '$ xx..yy'
]

# Welcome Message
print("Welcome! I'm your Python search assistant.")

while True:
    # Present the available sets of operators to the user
    print("Choose an operator set:")
    for index, operator_set in enumerate(operator_sets.keys(), start=1):
        print(f"{index}. {operator_set}")
   
    # Ask the user to select an operator set
    selected_set = None
    while selected_set is None:
        try:
            user_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= user_choice <= len(operator_sets):
                selected_set = list(operator_sets.keys())[user_choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")    
    # Present the operators in the selected set
    print(f"{selected_set}:")
    for index, operator in enumerate(operator_sets[selected_set], start=1):
        print(f"{index}. {operator}")
 
    query_elements = []
    # Ask the user to select an operator from the chosen set
    selected_operator = None
    while selected_operator is None:
        try:
            user_choice = int(input("Enter the number corresponding to your chosen operator (or 0 to skip): ")) # pylint: disable=line-too-long
            if 0 <= user_choice <= len(operator_sets[selected_set]):
                selected_operator = operator_sets[selected_set][user_choice - 1] if user_choice != 0 else "" # pylint: disable=line-too-long
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Verifica si el operador seleccionado requiere dos consultas
    if selected_operator in operators_requiring_two_queries:
        query1 = input("Enter the first query: ")
        query2 = input("Enter the second query: ")
        # Combina las dos consultas según sea necesario para el operador seleccionado
        if selected_operator in operator_processors:
            processed_query = operator_processors[selected_operator](query1, query2)
        else:
            processed_query = f"{query1} {selected_operator} {query2}"
    else:
    # Ask the user to enter separate elements for the search query
        query_elements = []
        while True:
            element = input("Enter a search element (or 'done' to finish, 'change' to choose another operator set): ") # pylint: disable=line-too-long
            if element.lower() == 'done':
                break
            if element.lower() == 'change':
                break  # Exit the element input loop to choose another operator set
            query_elements.append(element)   
    # Combine the elements into a single query
    combined_query = " ".join(query_elements) if query_elements else ""
    # Process the user's query based on the selected operator
    if selected_operator in operator_processors:
        processed_query = operator_processors[selected_operator](combined_query)
    else:
        processed_query = combined_query
    # Perform the Google search
    google_search(processed_query)
    # Ask if the user wants to choose another operator set or continue entering search elements
    another_set = input("Do you want to choose another operator set? (yes/no): ")
    if another_set.lower() != 'yes':
        break
