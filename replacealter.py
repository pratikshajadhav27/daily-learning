class Solution:
    def replaceCharacter(self, s: str, oldChar: str, newChar: str) -> str:
        result = []
        for char in s:
            if char == oldChar:
                result.append(newChar)
            else:
                result.append(char)
        return "".join(result)