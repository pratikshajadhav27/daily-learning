def count_odd_numbers(n, array):
    # Count how many numbers in the array are odd
    count = 0
    for num in array:
        if num % 2 != 0:
            count += 1
    return count