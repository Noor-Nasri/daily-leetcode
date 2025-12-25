class Solution:
    # You want to select k children, which stops them from losing happiness
    # If someone has 1 happiness and you select them, you prevent the loss of 1 happiness
    # So the obv strategy is to select the top k children, to preserve as much as possible
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse = True)
        tot_selected = 0
        for ind in range(k):
            finalVal = max(0, happiness[ind] - ind) 
            tot_selected += finalVal
        
        return tot_selected
        