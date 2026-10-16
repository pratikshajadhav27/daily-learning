def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
        
    return binary

# Example Usage:
# print(decimal_to_binary(10))  # Output: "1010"