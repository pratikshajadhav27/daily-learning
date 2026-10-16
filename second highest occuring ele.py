from collections import Counter

def secondHighestOccurringElement(arr):
    c = Counter(arr).most_common()
    return min([x for x, f in c if f == c[1][1]]) if len(c) > 1 else -1