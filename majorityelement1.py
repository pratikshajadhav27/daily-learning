from collections import Counter
def majorityElement(nums) -> int:
    return Counter(nums).most_common(1)[0][0]