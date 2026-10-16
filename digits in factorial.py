import math

def digitsInFactorial(n: int) -> int:
    # 0! and 1! both have 1 digit
    if n <= 1:
        return 1
        
    # Sum the logarithms of numbers from 1 to n
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
        
    # Number of digits = floor(log10(n!)) + 1
    return math.floor(digits) + 1