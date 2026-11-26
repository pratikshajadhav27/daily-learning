def is_kaprekar_number(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    sq_str = str(n * n)
    d = len(str(n))
    right = int(sq_str[-d:])
    left = int(sq_str[:-d]) if sq_str[:-d] else 0
    return (left + right) == n and right > 0