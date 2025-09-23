class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for str in strs[1:]:
                if(i == len(str) or strs[0][i] != str[i]):
                    return strs[0][0:i]
        return strs[0]

if __name__ == "__main__":
    sol = Solution()
    strs = ["lower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))
