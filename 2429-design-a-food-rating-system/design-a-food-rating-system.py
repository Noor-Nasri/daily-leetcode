# So we just need to maintain a minheap that allows updates. Which is annoying in python.
# We can also implement the update function as a helper that takes the list implementation. Yuck.

# Heap util
from heapq import heappop, heappush

class FoodRatings:
    def addElement(self, cuisine, food, rating):
        if cuisine not in self.cuisineToPq:
            self.cuisineToPq[cuisine] = []

        entry = [-rating, food, cuisine]
        self.foodToElement[food] = entry
        heappush(self.cuisineToPq[cuisine], entry)

    def removeElement(self, food):
        # Remove food from our known list, and mark entry for future removal
        entry = self.foodToElement.pop(food)
        entry[-1] = ""

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineToPq = {}     
        self.foodToElement = {} 
        for i in range(len(foods)):
            self.addElement(cuisines[i], foods[i], ratings[i])

    def changeRating(self, food: str, newRating: int) -> None:
        _, _, cuisine = self.foodToElement[food]
        self.removeElement(food)
        self.addElement(cuisine, food, newRating)
        
    def highestRated(self, cuisine: str) -> str:
        while self.cuisineToPq[cuisine][0][-1] == "":
            # If the top food was supposed to be removed before, remove it now
            heappop(self.cuisineToPq[cuisine])
        
        return self.cuisineToPq[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)