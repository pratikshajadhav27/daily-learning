def reverseInteger(n: int) -> int:
    # Handle negative numbers by keeping track of the sign
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    # Reverse the digits by converting to string, reversing, and converting back to int
    reversed_num = int(str(n)[::-1]) * sign
    
    # Optional 32-bit integer overflow check if required by constraints
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
        
    return reversed_num