"""Main program entry point"""
from calculator import Calculator

def validate_number(value):
    """Validate if a string can be converted to a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_result(number):
    """Format number to remove .0 if it's a whole number"""
    return str(int(number)) if number.is_integer() else str(number)

def perform_calculation(a: str, b: str, operation: str) -> str:
    """Perform calculation and return formatted result string"""
    
    # Validate input numbers
    if not validate_number(a) or not validate_number(b):
        return f"Invalid number input: {a} or {b} is not a valid number."
    
    # Convert strings to numbers
    num_a = float(a)
    num_b = float(b)
    
    try:
        if operation == 'add':
            result = Calculator.add(num_a, num_b)
        elif operation == 'subtract':
            result = Calculator.subtract(num_a, num_b)
        elif operation == 'multiply':
            result = Calculator.multiply(num_a, num_b)
        elif operation == 'divide':
            result = Calculator.divide(num_a, num_b)
        else:
            return f"Unknown operation: {operation}"
        
        return f"The result of {a} {operation} {b} is equal to {format_result(result)}"
    except ZeroDivisionError as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    print(perform_calculation("5", "3", "add"))
    print(perform_calculation("1", "0", "divide"))