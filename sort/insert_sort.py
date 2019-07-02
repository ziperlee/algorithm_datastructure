"""
 Create by zipee on 2019/5/23.
"""
__author__ = "zipee"

from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    """
    插入排序
    时间复杂度：最好n，最差n2，平均n2
    空间复杂度：n
    原地排序，稳定排序
    :param nums:
    :return:
    """

    length = len(nums)
    for i in range(1, length):
        # j = i
        # while j > 0 and nums[j] < nums[j-1]:
        #     nums[j-1], nums[j] = nums[j], nums[j-1]
        #     j -= 1
        j = i - 1
        v = nums[i]
        while j >= 0 and nums[j] > v:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = v
    return nums


def test_insert_sort():
    test_array = [1, 1, 1, 1]
    insert_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [1]
    insert_sort(test_array)
    assert test_array == [1]
