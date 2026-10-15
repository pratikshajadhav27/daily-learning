def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Example Usage:
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]
# print(find_common_elements(l1, l2))  # Output: [4, 5]