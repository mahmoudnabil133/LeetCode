\\\
implement least frequent element cache
when cache is  full it removes the least freequent element
\\\


class Node:
    \\\
    node for dll
    \\\
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 1


class DlinkedList:
    \Dlinked list class\
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.tail

    def add_from_head(self, node):
        \add a node from head\
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        \remove node from list\
        node.prev.next = node.next
        node.next.prev = node.prev

    def delete_from_tail(self):
        \remove node from tail of the list\
        if self.head.next == self.tail:
            return -1
        to_remove = self.tail.prev
        self.remove_node(to_remove)
        return to_remove

    def len(self):
        \get length of the list\
        cur = self.head
        ans = 0
        while cur:
            cur = cur.next
            ans += 1
        return ans - 2

    def is_empty(self):
        \check if list is impty or not\
        if self.head.next == self.tail:
            return True
        return False


class LFUCache:
    \implement lfu cache\

    def __init__(self, capacity: int):
        self.cache_data = {}
        self.freq_map = {}
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        \get item from lfu cache and update cache frequency\
        if key not in self.cache_data:
            return -1
        node = self.cache_data[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        \update cache frequency or put new item to it\
        # if not key or not value:
        #     return
        if key in self.cache_data:
            node = self.cache_data[key]
            node.value = value
            self.update(node)

        else:

            if len(self.cache_data) >= self.capacity:
                least_freq_list = self.freq_map[self.min_freq]
                deleted_node = least_freq_list.delete_from_tail()

                if self.freq_map[self.min_freq].is_empty():
                    del self.freq_map[self.min_freq]
                    self.min_freq += 1

                del self.cache_data[deleted_node.key]
                print(f'DISCARD: {deleted_node.key}')
            new_node = Node(key, value)
            self.cache_data[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_map:
                self.freq_map[1] = DlinkedList()

            self.freq_map[1].add_from_head(new_node)

    def update(self, node):
        \update cache\
        old_freq = node.freq
        node.freq += 1

        # remove node from old freq
        self.freq_map[old_freq].remove_node(node)
        if self.freq_map[old_freq].len() == 0:
            if old_freq == self.min_freq:
                self.min_freq += 1
            del self.freq_map[old_freq]

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DlinkedList()

        self.freq_map[node.freq].add_from_head(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)