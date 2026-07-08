class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res = []
        for i in range(len(s_nums)): 
            if i > 0 and s_nums[i] == s_nums[i-1]: 
                continue
            a = s_nums[i]
            if a > 0: break
            j = i+1
            k = len(s_nums) - 1

            while(j<k):
                total = s_nums[i] + s_nums[j] + s_nums[k] 
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([s_nums[i],s_nums[j],s_nums[k]])
                    while j<k and s_nums[j] == s_nums[j+1]:
                        j += 1
                    while j<k and s_nums[k] == s_nums[k-1]:
                        k -= 1 
                    j += 1
                    k -=1
            
        return res
