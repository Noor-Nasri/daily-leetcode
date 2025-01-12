class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Constraint: You cannot put a closed bracket when none are open.
        # Imagine four unlocked options: You can get 0, 2, 4
        # ((((, (((), (()). 
        # Imagine 5 options: You can get 5, 3, 1
        # (((((,((((), ((()) 

        # Thus: 3 options give 1, 3
        # 4 options give 0, 2, 4
        # BUT: _, _, _, ) means we can have (()), (((). Thus 0, 2. 
        # OR: _, _, _, ( means we can have ((((, (()(. Thus 2, 4. 

        # _, _, )
        # At 2, we have 0, 2. So now we have only [1]

        low = 0
        high = 0

        for ind in range(len(locked)):

            if locked[ind] == '1':
                if s[ind] == "(":
                    low += 1
                    high += 1
                    #print("Forced to open a path", low, high)
                    continue
                
                # check if this closed bracket makes it impossible
                if high == 0:
                    #print("Forced to die")
                    return False
                
                # For paths that lead to 0, we cannot pursue them. 
                # Then paths leading to 2 would become 1.
                if low: 
                    low -= 1
                else:
                    low = 1
 
                high -= 1
                #print("Our options got reduced to", low, high)
            
            else:
                if low: 
                    low -= 1
                else:
                    # cannot put a closed bracket if no prev brackets. Thus only open
                    low = 1

                high += 1 # can always open another bracket
                #print("Our options branched to", low, high)
        
        #print("finale", low, high)
        return low == 0
                




    
        