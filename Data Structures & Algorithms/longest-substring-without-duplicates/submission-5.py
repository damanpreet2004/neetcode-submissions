class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prefix = ""
        pre_len = 0
        c_win = ""
        l = 0 
        for i in range(len(s)):
            if s[i] not in c_win:
                c_win += s[i]
            else:
                duplicate = c_win.index(s[i])
                l += duplicate + 1
                c_win = c_win[duplicate + 1 :] + s[i]
            if ((i+1) - l) > pre_len:
                pre_len = (i+1) - l
                
        return pre_len
