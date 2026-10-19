def largestOddNumber(s: str) -> str:
    # Handle dictionary input format safely
    if isinstance(s, dict):
        s = str(s.get("s", ""))
    else:
        s = str(s)
    
    # Traverse from right to left
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i + 1]
            
    return ""