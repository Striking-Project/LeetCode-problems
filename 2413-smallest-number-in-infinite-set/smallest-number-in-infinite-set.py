import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.added_back = []  
        self.current = 1      

    def popSmallest(self) -> int:
        if self.added_back and self.added_back[0] < self.current:
            return heapq.heappop(self.added_back)
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back:
            heapq.heappush(self.added_back, num)
