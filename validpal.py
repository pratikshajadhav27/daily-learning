def isPalindrome(s: str) -> bool:
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the filtered string equals its reverse
    return filtered == filtered[::-1]