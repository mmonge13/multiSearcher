# Import the operator_sets and operator_processors from operator.py
from operators import operator_sets
# Import the operator_sets and operator_processors from operator.py
from operators import operator_processors
# Import the google_search function from search.py
from search import google_search

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
            user_choice = int(
                input("Enter the number corresponding to your choice: "))
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

    # Ask the user to select an operator from the chosen set
    selected_operator = None
    while selected_operator is None:
        try:
            user_choice = int(
                input("Enter the number corresponding to your chosen operator (or 0 to skip): "))
            if 0 <= user_choice <= len(operator_sets[selected_set]):
                selected_operator = operator_sets[selected_set][user_choice -
                                                                1] if user_choice != 0 else ""
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask the user to enter separate elements for the search query
    query_elements = []
    while True:
        element = input(
            "Enter a search element (or 'done' to finish, 'change' to choose another operator set): ")
        if element.lower() == 'done':
            break
        elif element.lower() == 'change':
            break  # Exit the element input loop to choose another operator set
        query_elements.append(element)

    # Combine the elements into a single query
    combined_query = " ".join(query_elements)

    # Process the user's query based on the selected operator
    if selected_operator in operator_processors:
        processed_query = operator_processors[selected_operator](
            combined_query)
    else:
        processed_query = combined_query

    # Perform the Google search
    google_search(processed_query)

    # Ask if the user wants to choose another operator set or continue entering search elements
    another_set = input(
        "Do you want to choose another operator set? (yes/no): ")
    if another_set.lower() != 'yes':
        break
