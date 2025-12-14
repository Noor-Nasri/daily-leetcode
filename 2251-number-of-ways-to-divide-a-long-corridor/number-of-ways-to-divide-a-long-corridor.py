class Solution:
    # Since its exactly 2 seats, we know exactly which parts are stuck together
    # So just figure out the number of options between each group, and we get the product
    def numberOfWays(self, corridor: str) -> int:
        totalOptions = 1
        numPlants = 0
        numSeats = 0
        for item in corridor:
            if item == 'P':
                numPlants += 1
            elif numSeats < 2:
                numPlants = 0
                numSeats += 1
            else:
                totalOptions *= numPlants + 1
                totalOptions %= 10**9 + 7
                numSeats = 1
        
        if numSeats != 2:
            return 0
        return totalOptions
        


        