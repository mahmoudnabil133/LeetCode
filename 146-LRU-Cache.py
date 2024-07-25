class LRUCache:

    def __init__(self, capacity: int):
        self.__cache = OrderedDict()
        self.cap = capacity
    def get(self, key: int) -> int:
        if self.__cache.get(key, None) == None:
            return - 1
        self.__cache.move_to_end(key)
        return self.__cache[key]
    def put(self, key: int, value: int) -> None:
        if self.__cache.get(key, None) == None and len(self.__cache) >= self.cap:
            self.__cache.popitem(0)
        self.__cache[key] = value
        self.__cache.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)