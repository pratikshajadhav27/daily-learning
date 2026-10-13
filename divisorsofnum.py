def findDivisors(n):
    if isinstance(n, dict):
        n = list(n.values())[0]
    
    return sorted(list(set(i for i in range(1, int(n**0.5) + 1) if n % i == 0 for i in (i, n // i))))