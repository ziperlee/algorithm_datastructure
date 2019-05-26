"""
 Create by zipee on 2019/5/25.
"""
__author__ = "zipee"

from typing import List


def merge_sort(a: List[int]) -> List[int]:
    _merge_sort(a, 0, len(a) - 1)


def _merge_sort(a: List[int], l: int, r: int):
    if l >= r:
        return
    mid = l + (r - l >> 1)
    _merge_sort(a, l, mid)
    _merge_sort(a, mid + 1, r)
    merge(a, l, mid, r)


def merge(a: List[int], l: int, mid: int, r: int):
    i, j = l, mid + 1
    tmp = []
    while i <= mid and j <= r:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else r
    tmp.extend(a[start : end + 1])
    a[l : r + 1] = tmp


def test_merge_sort():
    # test_array = [1, 1, 1, 1]
    # merge_sort(test_array)
    # assert test_array == [1, 1, 1, 1]
    # test_array = [4, 1, 2, 3]
    # merge_sort(test_array)
    # assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    merge_sort(test_array)
    # assert test_array == [1, 2, 3, 4]
    # test_array = [1]
    # merge_sort(test_array)
    # assert test_array == [1]
