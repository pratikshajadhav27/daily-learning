from collections import Counter

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    result = []
    
    for num in count1:
        if num in count2:
            # Common element ko minimum frequency jitni baar add karte hain
            result.extend([num] * min(count1[num], count2[num]))
            
    return result