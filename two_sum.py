#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSun(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]


nums = [3, 2, 4]
target = 6
s = Solution()
print(s.twoSun(nums, target))
