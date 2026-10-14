def transpose_matrix(matrix):
    # Using list comprehension to swap rows and columns
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example Usage:
# mat = [[1, 2, 3], 
#        [4, 5, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]