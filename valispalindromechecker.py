def is_palindrome(s: str) -> bool:
    # Special characters aur spaces hata kar lowercase banata hai
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    if is_palindrome(test_str):
        print(f'"{test_str}" is a valid palindrome!')
    else:
        print(f'"{test_str}" is NOT a palindrome.')