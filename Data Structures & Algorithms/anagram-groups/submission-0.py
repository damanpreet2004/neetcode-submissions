class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        seen = [False] * len(strs)
        for i in range(len(strs)):
            if seen[i]: continue
            items = []
            for j in range(i, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    seen[j] = True
                    items.append(strs[j])

            result.append(items)
                    
                    
        return result