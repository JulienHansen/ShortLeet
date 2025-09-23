class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        counter = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                counter += 1
            else:
                i += 1
        return counter, nums



if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(sol.removeElement(nums, val))

