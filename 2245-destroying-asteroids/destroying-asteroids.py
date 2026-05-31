class Solution:
    # Why wouldn't we just always absorb the smallest astroid each time?
    # Seems like an easy unless I am missing something..
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        for hit in asteroids:
            if hit <= mass:
                mass += hit
            else:
                return False
        
        return True