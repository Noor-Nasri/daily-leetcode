from heapq import heapify, heappush, heappop 

class KthLargest:
    largestKElements = None

    def createMinHeap(self):
        self.largestKElements = sorted(self.nums)[-self.k:] # start with top k elements
        heapify(self.largestKElements)


    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        if self.largestKElements == None:
            # cuz we have enough elements on the first call
            self.nums.append(val)
            self.createMinHeap()
    
        elif val > self.largestKElements[0]:
            heappop(self.largestKElements)
            heappush(self.largestKElements, val)
        
        return self.largestKElements[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)