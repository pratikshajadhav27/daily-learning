from collections import Counter

def sumOfFrequencies(arr):
    v = list(Counter(arr).values())
    return max(v) + min(v)