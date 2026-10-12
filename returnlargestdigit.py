def returnLargestDigit(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
        
    max_digit = 0
    while n > 0:
        digit = n % 10
        if digit > max_digit:
            max_digit = digit
        n //= 10
        
    return max_digit