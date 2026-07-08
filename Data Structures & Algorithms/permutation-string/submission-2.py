class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        for i in range(len(s2)):
            if str(''.join(sorted(s1))) in str(''.join(sorted(s2[i : i + len(s1)]))):
                res =  True
                break
            else:
                res = False
        return res