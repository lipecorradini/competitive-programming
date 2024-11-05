class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split()

        return len(new_s[-1])