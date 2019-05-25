"""
 Create by zipee on 2019/4/5.
"""
__author__ = "zipee"

from collections import deque


class Stack1:
    """
    后进先出
    """

    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()


class Stack2:
    """
    后进先出
    """

    def __init__(self):
        self.stack = list()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()


class TestStack:
    def test_stack1(self):
        s = Stack1()
        s.push(1)
        s.push(2)
        s.push(3)

        assert 3 == s.pop()
        assert 2 == s.pop()
        assert 1 == s.pop()

    def test_stack2(self):
        s = Stack2()
        s.push(1)
        s.push(2)
        s.push(3)

        assert 3 == s.pop()
        assert 2 == s.pop()
        assert 1 == s.pop()
