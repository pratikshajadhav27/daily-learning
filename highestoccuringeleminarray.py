from collections import Counter

def highestOccurringElement(nums):
    c = Counter(nums).most_common()
    return min([x for x, f in c if f == c[0][1]])