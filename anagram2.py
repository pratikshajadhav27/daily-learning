from collections import Counter  # 1. VS Code ke liye import zaroori hai

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return Counter(s) == Counter(t)

# 2. Code ko run karke result dekhne ke liye:
print(isAnagram(None, "anagram", "nagaram"))