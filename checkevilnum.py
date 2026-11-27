def is_evil_number(n):
    if n < 0:
        return False
    binary_str = bin(n)[2:]
    ones_count = binary_str.count("1")
    return ones_count % 2 == 0