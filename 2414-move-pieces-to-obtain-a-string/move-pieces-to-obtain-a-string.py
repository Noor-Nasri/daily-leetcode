class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Two pointer:
        # Idea: relative positioning of L and Rs will stay the same. Can just shift around.
        # Impossible if: 
        # - inequal relative positioning
        # - at any ind, there is more L in start than target. 
        # - at any ind, there is more R in target than in start.

        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        count_start = {"L": 0, "R": 0, "_": 0}
        count_target = {"L": 0, "R": 0, "_": 0}

        for ind in range(len(start)):
            count_start[start[ind]] += 1
            count_target[target[ind]] += 1

            if count_start["L"] > count_target["L"]:
                return False
            
            if count_start["R"] < count_target["R"]:
                return False 

        return True        