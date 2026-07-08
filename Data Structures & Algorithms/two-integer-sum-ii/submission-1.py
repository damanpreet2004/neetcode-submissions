class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1
        res = [] 
        for i in range(len(numbers)):
            if len(res) == 2: break
            for j in range(len(numbers)):
                if i == j: continue
                if (numbers[i] + numbers[j]) == target:
                    res.append(i+1)
                    res.append(j+1)
        return res
