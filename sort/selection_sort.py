"""
 Create by zipee on 2019/5/23.
"""
__author__ = "zipee"

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    for i in range(length - 1):
        min = i
        for j in range(i + 1, length):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    selection_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    selection_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [1]
    selection_sort(test_array)
    assert test_array == [1]
