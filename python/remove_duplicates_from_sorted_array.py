# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 26

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums: int = len(nums)
        # Обработка крайних случаев
        if len_nums == 1:
            return 1
        # Вводим дополнительную переменную - для уникальных элементов
        i: int = 0
        # Выполнение замены
        for j in range(1, len_nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
