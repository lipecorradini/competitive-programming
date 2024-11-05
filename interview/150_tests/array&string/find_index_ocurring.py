class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tam = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + tam <= len(haystack) and haystack[i:i+tam] == needle:
                    return i

        return -1