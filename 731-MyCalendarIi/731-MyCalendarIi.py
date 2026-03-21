# Last updated: 3/22/2026, 12:45:46 AM
class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for os, oe in self.overlaps:
            if max(start, os) < min(end, oe):
                return False 
        for bs, be in self.bookings:
            if max(start, bs) < min(end, be):
                self.overlaps.append((max(start, bs), min(end, be)))
        self.bookings.append((start, end))
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
#obj = MyCalendarTwo()
#param_1 = obj.book(start,end)