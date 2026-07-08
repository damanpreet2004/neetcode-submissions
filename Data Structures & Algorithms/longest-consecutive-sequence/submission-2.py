class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        num_set = set(nums)
        max_length = 0
        if len(nums) == 0:
            return 0
        else:
            for i in num_set:
                if (i-1) not in num_set:
                    current_num = i
                    current_length = 1
                    while(current_num+1 in num_set):
                        current_num += 1
                        current_length += 1
                    max_length = max(max_length,current_length)


        return max_length
