class Solution:
    # So the way we solve this is by solving the left-most at a time, meaning we need to create 1100..00
    # So that means we need to first turn the n-2 into 00..00. I see a recurive nature here but its odd
    # Can I just simulate this? Its only 30 bits. 
    # Once we solve the first bit, then we just have a 1000..000 structure. There should be a formula for this
    # Honestly hard for me to visualize, but we can just memoize whch will auto solve after first bit!
    
    def solveWithLameMemoize(self, curBits, desiredFirstDigit):
        # Returns min # of moves to turn bits into desired0000..00

        if (curBits, desiredFirstDigit) in self.sols:
            return self.sols[(curBits, desiredFirstDigit)]
        elif len(curBits) == 1:
            return int(curBits[0] != desiredFirstDigit)

        firstDigit = curBits[0]
        remDigits = curBits[1:]
        if firstDigit == desiredFirstDigit:
            self.sols[(curBits, desiredFirstDigit)] = self.solveWithLameMemoize(remDigits, 0)
        else:
            step1 = self.solveWithLameMemoize(remDigits, 1) # Make rest 1000.00
            # Step 2 is just to flip our first digit
            digitsToUndo = tuple([1] + [0]*(len(remDigits) - 1)) 
            step3 = self.solveWithLameMemoize(digitsToUndo, 0)
            self.sols[(curBits, desiredFirstDigit)] = step1 + 1 + step3

        return self.sols[(curBits, desiredFirstDigit)]

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        bits = [int(e) for e in str(bin(n))[2:]]
        bits = tuple(bits[bits.index(1):])
        self.sols = {}
        return self.solveWithLameMemoize(bits, 0)
        