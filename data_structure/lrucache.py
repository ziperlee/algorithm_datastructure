"""
 Create by zipee on 2019/6/26.
"""
__author__ = "zipee"

from collections import OrderedDict


class LRUCache:
    """least recently used cache
        当缓存不够用时，先剔除最近最少使用的对象"""

    def __init__(self, capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        return -1

    def put(self, key, val):
        if key in self.od:
            del self.od[key]
            self.od[key] = val
        else:
            self.od[key] = val
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)

    def __repr__(self):
        return str(self.od)


def test_lrucache():
    lru = LRUCache(capacity=5)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    lru.put(5, 5)
    lru.put(6, 6)

    tmp = OrderedDict({2: 2, 3: 3, 4: 4, 5: 5, 6: 6})
    assert str(lru) == str(tmp)

    lru2 = LRUCache(capacity=5)
    lru2.put(1, 1)
    lru2.put(2, 2)
    lru2.put(3, 3)
    lru2.put(4, 4)
    lru2.put(5, 5)
    lru2.get(1)
    lru2.put(6, 6)

    tmp = OrderedDict({3: 3, 4: 4, 5: 5, 1: 1, 6: 6})
    assert str(lru2) == str(tmp)
