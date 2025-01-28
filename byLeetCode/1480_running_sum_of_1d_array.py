"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
https://leetcode.com/problems/running-sum-of-1d-array/description/
"""


def running_sum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums
