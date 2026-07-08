class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for lp in range(len(nums)):
            for rp in range(lp + 1, len(nums)):
                if(nums[lp] + nums[rp] == target):
                    res = [lp,rp]
                    return res