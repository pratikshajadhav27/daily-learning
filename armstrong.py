def isArmstrong(n: int) -> bool:
    if n < 0:
        return False
        
    original = n
    # Find the number of digits
    num_digits = len(str(n)) if n > 0 else 1
    
    total_sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** num_digits
        temp //= 10
        
    return total_sum == original