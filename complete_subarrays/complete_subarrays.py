class Solution(object):
    def countCompleteSubarrays(self, nums): 
        n = len(nums); total_distinct = len(set(nums)); cnt = 0; ans = 0; j = 0 
        freq = {}    
        for i in range(n):
            while j < n and cnt < total_distinct:
                if freq.get(nums[j], 0) == 0:
                    cnt += 1
                freq[nums[j]] = freq.get(nums[j], 0) + 1
                j += 1
            if cnt == total_distinct:
                ans += (n - j + 1)
            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                cnt -= 1
        return ans

