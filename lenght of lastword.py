def lengthOfLastWord(s: str) -> int:
    words = s.split()
    if not words:
        return 0
    return len(words[-1])