class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1               

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,3,4]
    print(sol.removeDuplicates(nums))

