class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        key_list = [key for key, count in freq.most_common()]        
        for i in range(len(key_list)):
            if k == 0:
                break
            else:
                res.append(key_list[i])
                k = k-1
        return res
