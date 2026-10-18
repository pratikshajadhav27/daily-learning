def roundToNearest(s: str) -> int:
    # Convert the input string to an integer
    num = int(s)
    
    # Find the remainder when divided by 10
    remainder = num % 10
    
    if remainder < 5:
        # Round down to the lower multiple of 10
        result = num - remainder
    elif remainder > 5:
        # Round up to the higher multiple of 10
        result = num + (10 - remainder)
    else:
        # Exactly 5: tie-breaking rule (return the smaller multiple)
        result = num - remainder
        
    return result