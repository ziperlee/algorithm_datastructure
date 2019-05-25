"""
 Create by zipee on 2019/4/5.
"""
__author__ = "zipee"

from collections import deque


class Queue1:
    """
    先进先出
    """

    def __init__(self):
        self.q = deque()

    def push(self, val):
        self.q.append(val)

    def pop(self):
        return self.q.popleft()


class Queue2:
    """
    先进先出
    """

    def __init__(self):
        self.q = list()

    def push(self, val):
        self.q.append(val)

    def pop(self):
        res = self.q[0]
        self.q = self.q[1:]
        return res


class TestQueue:
    def test_queue1(self):
        q = Queue1()
        q.push(1)
        q.push(2)
        q.push(3)

        assert 1 == q.pop()
        assert 2 == q.pop()
        assert 3 == q.pop()

    def test_queue2(self):
        q = Queue1()
        q.push(1)
        q.push(2)
        q.push(3)

        assert 1 == q.pop()
        assert 2 == q.pop()
        assert 3 == q.pop()
