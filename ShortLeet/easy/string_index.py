class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for c in haystack:
            print(c)
        



if __name__ == "__main__":
    sol = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))
