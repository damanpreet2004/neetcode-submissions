class Solution:
    def isValid(self, s: str) -> bool:
        dict_m = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        stack = ["-1"]
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if dict_m.get(stack[-1]) == s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
        if len(stack) == 1:
            return True
        else:
            return False