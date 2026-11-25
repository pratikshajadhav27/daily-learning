def is_pronic_number(n):
    if n < 0:
        return False
    k = 0
    while k * (k + 1) <= n:
        if k * (k + 1) == n:
            return True
        k += 1
    return False