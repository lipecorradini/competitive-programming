class Solution:
    # O(1) space and O(n) time complexity optimal solution
    def majorityElement(self, nums: List[int]) -> int:
        cont = 0
        max_num = 0

        for i in range(len(nums)):
            if cont == 0:
                max_num = nums[i]
                cont += 1
            elif nums[i] != max_num:
                cont -= 1
            else:
                cont += 1
        
        return max_num