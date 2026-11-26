def most_frequent_char(s):
    cleaned = s.replace(" ", "")
    if not cleaned:
        return None
    max_char = cleaned[0]
    max_count = 0
    for ch in cleaned:
        count = cleaned.count(ch)
        if count > max_count:
            max_count = count
            max_char = ch
    return max_char