class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Since n <= 500, we can just try each language and see how many people have to learn it.
        # Theres a lot in the description but it doesnt really matter. If they have any friends that dont share any languages, they need to learn whatever you pick
        nPeople = len(languages)
        languages = [set(e) for e in languages]
        needsToLearn = [False for i in range(nPeople)]
        for u, v in friendships:
            hasSharedLanguage = False
            for language in languages[u - 1]:
                if language in languages[v - 1]:
                    hasSharedLanguage = True
                    break
            
            if not hasSharedLanguage:
                needsToLearn[u - 1] = True
                needsToLearn[v - 1] = True
        
        leastNumToTeach = nPeople
        for language in range(1, n + 1):
            numToTeach = 0
            for person in range(nPeople):
                if needsToLearn[person] and language not in languages[person]:
                    numToTeach += 1
            
            leastNumToTeach = min(leastNumToTeach, numToTeach)
        
        return leastNumToTeach