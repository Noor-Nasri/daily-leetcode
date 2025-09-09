from collections import deque 
class Solution:
    # I feel like there is a closed form solution here, but n is 1000 so we can just simulate
    # On a given day, x people may learn the secret. Then, on day x + d, they will each share the secret to the next [f] people
    # So just two for loops with a list of counters

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        totalPeople = 0
        numPeopleDiscoverOnDay = [0 for i in range(n)]
        numPeopleDiscoverOnDay[0] = 1

        for day in range(n):
            if not numPeopleDiscoverOnDay[day]:
                continue
            
            revealDay = day + delay
            forgetDay = min(day + forget, n)
            for shareDay in range(revealDay, forgetDay):
                numPeopleDiscoverOnDay[shareDay] += numPeopleDiscoverOnDay[day]
                numPeopleDiscoverOnDay[shareDay] %= 10**9 + 7


            if forgetDay == n:
                # These people will still know the secret at the end of day n
                totalPeople += numPeopleDiscoverOnDay[day]
                totalPeople %= 10**9 + 7

        return totalPeople

        
        