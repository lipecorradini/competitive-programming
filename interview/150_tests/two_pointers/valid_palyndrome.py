class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if x.isalnum()]

        ini = 0
        final = len(s) - 1

        while ini < final:
            if s[ini] != s[final]:
                return False
            ini += 1
            final -= 1 
        
        return True


# Optimal Solution
