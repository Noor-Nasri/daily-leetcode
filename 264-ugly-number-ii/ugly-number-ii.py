class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies_list = [1, 2, 3, 5]
        uglies_set = set(uglies_list)

        while len(uglies_set) < n*10:
            nextUglies = []
            for ugly in uglies_list:
                for mult in [2, 3, 5]:
                    nextUgly = ugly*mult
                    if nextUgly in uglies_set: continue
                    uglies_set.add(nextUgly)
                    nextUglies.append(nextUgly)
            
            uglies_list = nextUglies
            
        truth = sorted(list(uglies_set))
        return truth[n-1]
        

        