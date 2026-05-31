# Last updated: 5/31/2026, 11:37:08 PM
1from collections import OrderedDict
2
3class LRUCache:
4
5    def __init__(self, capacity):
6        self.cap = capacity
7        self.cache = OrderedDict()
8
9    def get(self, key):
10        if key not in self.cache:
11            return -1
12
13        self.cache.move_to_end(key)
14        return self.cache[key]
15
16    def put(self, key, value):
17        if key in self.cache:
18            self.cache.move_to_end(key)
19
20        self.cache[key] = value
21
22        if len(self.cache) > self.cap:
23            self.cache.popitem(last=False)
24        
25
26
27# Your LRUCache object will be instantiated and called as such:
28# obj = LRUCache(capacity)
29# param_1 = obj.get(key)
30# obj.put(key,value)