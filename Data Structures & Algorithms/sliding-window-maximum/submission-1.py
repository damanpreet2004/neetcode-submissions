class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1 
        temp = []
        res = []
        while(r < len(nums)):
            temp = sorted(nums[l:r+1])
            res.append(temp[len(temp) - 1])
            l += 1
            r += 1
        return res