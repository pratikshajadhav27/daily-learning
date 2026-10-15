
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    total_sum = sum(int(digit) ** n for digit in num_str)
    return total_sum == num

# Example Usage:
# print(is_armstrong(153))  # Output: True (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
# print(is_armstrong(120))  # Output: False