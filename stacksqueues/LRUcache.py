#Do not use list instead use dictionary
#Use ordered dictionary to maintain the order so that get and put methods are handled efficiently
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value=self.cache.pop(key)
        self.cache[key]=value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache)==self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)