# https://leetcode.com/problems/shuffle-the-array/
# 1470. Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        c = [0] * 2 * n
        for i in range(n):
            c[i * 2] = nums[i]
            c[i * 2 + 1] = nums[n + i]
        return c
