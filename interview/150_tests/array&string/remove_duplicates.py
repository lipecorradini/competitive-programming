class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        position = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:position]:
                nums[position] = nums[i]
                position += 1
        
        return position

# Optimal solution
# Como está ordenado, posso comparar apenas com o número anterior, ao invés de com todos os outros

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j