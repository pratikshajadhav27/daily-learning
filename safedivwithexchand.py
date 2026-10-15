def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input types! Please provide numbers."
    else:
        return f"Success! Result is: {result}"
    finally:
        print("Execution completed.")

# Example Usage:
# print(safe_divide(10, 2))   # Output: Success! Result is: 5.0
# print(safe_divide(10, 0))   # Output: Error: Cannot divide by zero!