"""
 Create by zipee on 2019/5/25.
"""
__author__ = "zipee"

from typing import List


def quick_sort(a: List[int]) -> List[int]:
    # _quick_sort1(a, 0, len(a)-1)
    _quick_sort2(a, 0, len(a) - 1)


def _quick_sort1(a: List[int], l: int, r: int):
    if l < r:
        p = _partition(a, l, r)
        _quick_sort1(a, l, p - 1)
        _quick_sort1(a, p + 1, r)


def _partition(a: List[int], l: int, r: int):
    pivot = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i


def _quick_sort2(a: List[int], l: int, r: int):
    """
    左右指针法
    :param a:
    :param l:
    :param r:
    :return:
    """
    pivot = a[r]
    i, j = l, r
    while i < j:
        while i < j and a[i] <= pivot:
            i += 1
        while i < j and a[j] >= pivot:
            j -= 1
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    if i > l + 1:
        _quick_sort2(a, l, i - 1)
    if i < r - 1:
        _quick_sort2(a, i + 1, r)


def test_quick_sort():
    a = [1, 1, 1, 1]
    quick_sort(a)
    assert a == [1, 1, 1, 1]
    a = [4, 1, 2, 3]
    quick_sort(a)
    assert a == [1, 2, 3, 4]
    a = [4, 3, 2, 1]
    quick_sort(a)
    assert a == [1, 2, 3, 4]
    a = [1]
    quick_sort(a)
    assert a == [1]
    a = [0, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1]
    quick_sort(a)
    print(a)
