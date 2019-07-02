from typing import List

def bubble_sort(nums:List[int])->List[int]:
    """
    冒泡排序
    时间复杂度：最好n，最差n2，平均n2
    空间复杂度：n
    原地排序，稳定排序
    :param nums:
    :return:
    """
    for i, _ in enumerate(nums):
        sorted = True
        for j, _ in enumerate(nums[:len(nums)-i-1]):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                sorted = False
        if sorted:
            break
    return nums


def test_bubble_sort():
    nums = [9,8,6,7,5,3,4,1,2,0]
    assert bubble_sort(nums) == [0,1,2,3,4,5,6,7,8,9]
    nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bubble_sort(nums2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]