# 238 - Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of
# all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate prefix first then calculate postfix using the same result array
        Prefix = multiplication of all values before the index
        Prefix = multiplication of all after before the index
        Time: O(n)
        Space: Optimized to have O(1) memory complexity
        """

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate prefix and postfix of nums
        Then, for each index, we will multiply values at prefix[index] and postfix[index]
        Time: O(n)
        Space: O(n)
        """
        # nums = [1, 2, 3, 4]
        length = len(nums)
        res, prefix, postfix = [0] * length, [0] * length, [0] * length

        prefix[0] = 1
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # prefix = [1]
        # i = 1, prefix = [1, 1]
        # i = 2, prefix = [1, 1, 2]
        # i = 3, prefix = [1, 1, 2, 6]

        postfix[length - 1] = 1
        for i in reversed(range(length - 1)):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        # postfix = [1]
        # i = 2, postfix = [4, 1]
        # i = 1, postfix = [12, 4, 1]
        # i = 0, postfix = [24, 12, 4, 1]

        for i in range(length):
            res[i] = prefix[i] * postfix[i]

        return res

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]