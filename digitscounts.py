class Solution:
    def digitCounts(self, n: int) -> int:
        # Handle the case for 0 explicitly since log10(0) is undefined
        if n == 0:
            return 1
        
        # Convert the number to a string and return its length
        return len(str(abs(n)))