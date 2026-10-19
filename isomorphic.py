def isIsomorphic(s: str, t: str) -> bool:
    # Handle dictionary input wrapper if passed by the platform
    if isinstance(s, dict):
        t = s.get("t", "")
        s = s.get("s", "")
        
    if len(s) != len(t):
        return False
        
    map_s_to_t = {}
    map_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check if mapping from s to t already exists and conflicts
        if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
            return False
        # Check if mapping from t to s already exists and conflicts
        if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
            return False
            
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s
        
    return True