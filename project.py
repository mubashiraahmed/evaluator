import re

def is_valid_expression(expression):
    """
    Validate the expression to allow only numbers, operators, and parentheses.
    """
    pattern = r"^[0-9+\-*/().\s]+$"
    return bool(re.match(pattern, expression))

def evaluate_expression():
    print("Welcome to the Enhanced Expression Evaluator!")
    print("You can use +, -, *, /, **, and parentheses.")
    print("Type 'exit' to quit.\n")

    while True:
        # Input expression from the user
        expression = input("Enter expression: ").strip()

        # Exit condition
        if expression.lower() == "exit":
            print("Goodbye!")
            break

        # Validate the expression
        if not is_valid_expression(expression):
            print("Error: Invalid characters in expression. Please try again.")
            continue

        try:
            # Evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error: Could not evaluate the expression ({e}).")

if __name__ == "__main__":
    evaluate_expression()
