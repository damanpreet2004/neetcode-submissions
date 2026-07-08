class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                temp = temp * nums[j]
            result.append(temp)
            temp = 1
        return result