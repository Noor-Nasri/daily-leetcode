class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counters = {}
        for num in nums:
            if not num in counters: 
                counters[num] = 1
            else:
                counters[num] += 1
        
        frquencies = [[] for i in range(101)]
        for val in counters:
            frquencies[counters[val]].append(val)
        
        results = []
        for freq in range(1, 101):
            if not frquencies[freq]: continue
            items = sorted(frquencies[freq], reverse = True)

            for item in items:
                results += [item]*freq
            
        return results