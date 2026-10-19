def longestCommonPrefix(str) -> str:
    # Safely handle if input is passed as a dictionary or list
    if isinstance(str, dict):
        strs = str.get("str", [])
    else:
        strs = str
        
    if not strs:
        return ""
        
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_len = min(len(first), len(last))
    
    for i in range(min_len):
        if first[i] != last[i]:
            return first[:i]
            
    return first[:min_len]