class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        pre = []
        suf = []
        max_p = 0
        max_s = 0
        j = len(height) - 1
        for i in range(len(height)):
            pre.append(max_p)
            suf.append(max_s)
            if height[i] > max_p:
                max_p = height[i]
            if height[j] > max_s:
                max_s = height[j]
            j -= 1
        suf = suf[::-1]
        for i in range(len(height)):
            current_area = min(pre[i], suf[i]) - height[i]
            if current_area < 0:
                current_area = 0
            area += current_area
        return area
             
            