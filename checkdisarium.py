def is_disarium_number(n):
    if n < 0:
        return False
    digits = str(n)
    total = 0
    for pos, ch in enumerate(digits, start=1):
        total += int(ch) ** pos
    return total == n