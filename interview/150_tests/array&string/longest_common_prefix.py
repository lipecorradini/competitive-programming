class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        
        min_len = 201
        for j in strs:
            if len(j) < min_len:
                min_len = len(j)
        
        if min_len == 0:
            return ""
        
        while i < min_len:
            first = strs[0][i]
            for word in strs:
                if word[i] != first:
                    return strs[0][:i]
            
            
            i+=1
        
        return strs[0][:i]

            
# Optimal solution
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
