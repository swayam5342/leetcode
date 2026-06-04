# Last updated: 6/5/2026, 3:01:04 AM
1class Foo:
2    def __init__(self):
3        self.l1 = 0
4        self.l2 = 0
5
6        pass
7
8
9    def first(self, printFirst: 'Callable[[], None]') -> None:
10        
11        # printFirst() outputs "first". Do not change or remove this line.
12        printFirst()
13        self.l1=1
14
15
16    def second(self, printSecond: 'Callable[[], None]') -> None:
17        while not self.l1:
18            ...
19        # printSecond() outputs "second". Do not change or remove this line.
20        printSecond()
21        self.l2=1
22
23
24    def third(self, printThird: 'Callable[[], None]') -> None:
25        while not self.l2:
26            ...
27        # printThird() outputs "third". Do not change or remove this line.
28        printThird()