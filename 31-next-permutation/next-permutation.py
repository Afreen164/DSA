
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)

        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find the smallest element greater than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
