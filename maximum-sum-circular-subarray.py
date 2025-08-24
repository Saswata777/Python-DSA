class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total_sum = sum(nums)

        def kadane(nums):
            curr_sum = nums[0]
            max_sum = nums[0]

            for i in range(1, len(nums)):
                curr_sum = max(nums[i], curr_sum + nums[i])
                max_sum = max(curr_sum, max_sum)
            return max_sum

        def kadane_min(nums):
            curr_sum = nums[0]
            min_sum = nums[0]

            for i in range(1, len(nums)):
                curr_sum = min(nums[i], curr_sum + nums[i])
                min_sum = min(curr_sum, min_sum)
            return min_sum

        max_normal = kadane(nums)
        min_normal = kadane_min(nums)

        # Handle edge case: all numbers negative
        if max_normal < 0:
            return max_normal

        circular_sum = total_sum - min_normal
        return max(max_normal, circular_sum)


