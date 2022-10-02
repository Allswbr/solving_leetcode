# https://leetcode.com/problems/rotate-array/
# 189

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Длина nums
        len_nums = len(nums)
        # Количество поворотов
        k = k % len_nums
        # Место среза
        slice_ = len_nums - k
        # Решение
        nums[:] = nums[slice_:] + nums[:slice_]