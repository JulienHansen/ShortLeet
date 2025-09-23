class Solution(object):
    def longestPalindrome(self, s): 
        if not s:
            return ""
        best_start, best_len = 0, 1

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1  

        for i in range(len(s)):
            start1, len1 = expand_around_center(i, i)
            if len1 > best_len:
                best_start, best_len = start1, len1
            start2, len2 = expand_around_center(i, i+1)
            if len2 > best_len:
                best_start, best_len = start2, len2
        return s[best_start:best_start + best_len]
