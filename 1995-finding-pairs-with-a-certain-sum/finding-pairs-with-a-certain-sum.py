class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.mainList = nums1
        self.secondaryList = nums2
        self.secondaryCounts = {}
        for num in nums2:
            self.secondaryCounts[num] = self.secondaryCounts.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        oldNum = self.secondaryList[index]
        newNum = oldNum + val
        self.secondaryCounts[oldNum] = self.secondaryCounts[oldNum] - 1
        self.secondaryCounts[newNum] = self.secondaryCounts.get(newNum, 0) + 1
        self.secondaryList[index] = newNum

    def count(self, tot: int) -> int:
        found = 0
        for num in self.mainList:
            needed = tot - num
            found += self.secondaryCounts.get(needed, 0) 

        return found



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)