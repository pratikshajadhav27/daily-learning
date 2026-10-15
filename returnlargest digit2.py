def returnLargestDigit(n):
    # Handle the special case where n is 0
    if n == 0:
        return 0
        
    largest = 0
    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n = n // 10
    return largest