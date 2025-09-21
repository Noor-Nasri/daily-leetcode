# gah, I misread this the first round and so the implementation is not clean. 

# We want 2 types of heaps.One for each specific movie to track their best rate, and one for all rented movies for our report
# When a movie is rented, we can just mark the node as used in the movie heap and add it to the rented heap.
# When a movie comes back, we just mark it in the rented heap and put a new one in the movie heap.
# So each rent results in just a push and one pop later on, and each drop does the same.


from heapq import heappush, heappop
class MovieRentingSystem:
    def addMovieListing(self, price, shop, movie):
        if movie not in self.movieToShopPq:
            self.movieToShopPq[movie] = []
        
        searchEntry = [price, shop, True]
        heappush(self.movieToShopPq[movie], searchEntry)
        self.entryDatabase[(shop, movie)] = [searchEntry, price]

    def peekTop5(self, pq):
        topEntries = []
        while pq and len(topEntries) < 5:
            entry = heappop(pq)
            if entry[-1]:
                topEntries.append(entry)
        
        for entry in topEntries:
            heappush(pq, entry)
        
        return topEntries

    def __init__(self, n: int, entries: List[List[int]]):
        self.movieToShopPq = {}
        self.rentalPq = []
        self.entryDatabase = {} # (Shop, Movie) = [active pqEntry, price]

        for shop, movie, price in entries:
            self.addMovieListing(price, shop, movie)

    def search(self, movie: int) -> List[int]:
        # Given movie, get 5 cheapest shops. Ie pop top 5 in movie heap
        if movie not in self.movieToShopPq:
            return []

        topEntries = self.peekTop5(self.movieToShopPq[movie])
        shops = [e[1] for e in topEntries]
        return shops


    def rent(self, shop: int, movie: int) -> None:
        searchEntry, price = self.entryDatabase[(shop, movie)]
        searchEntry[-1] = False
        rentEntry = [price, shop, movie, True]
        heappush(self.rentalPq, rentEntry)
        self.entryDatabase[(shop, movie)][0] = rentEntry
        

    def drop(self, shop: int, movie: int) -> None:
        rentEntry, price = self.entryDatabase[(shop, movie)]
        rentEntry[-1] = False
        searchEntry = [price, shop, True]
        heappush(self.movieToShopPq[movie], searchEntry)
        self.entryDatabase[(shop, movie)][0] = searchEntry
        

    def report(self) -> List[List[int]]:
        topEntries = self.peekTop5(self.rentalPq)
        shops = [[e[1], e[2]] for e in topEntries]
        return shops

        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()