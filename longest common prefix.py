def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    # Sort the array to compare only the first and last strings
    strs.sort()
    first = strs[0]
    last = strs[-1]
    
    min_len = min(len(first), len(last))
    for i in range(min_len):
        if first[i] != last[i]:
            return first[:i]
            
    return first[:min_len]