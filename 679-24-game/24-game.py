from itertools import permutations
magicExpr = "8/(3-(8/3))"

class Solution:
    def exploreAllOptions(self, curExpression, numOpenBrackets, numBracketsUsed, cardInd):
        # We decide the prefix opening brackets, suffix closing brackets, and suffix operation for each card
        if cardInd == 3:
            # Last number, just close any open brackets and check
            expr = "".join(curExpression + [self.cards[cardInd]] + [")"]*numOpenBrackets)
            try:
                answer = eval(expr)
            except ZeroDivisionError:
                answer = -1

            return abs(answer - 24) < 0.001
        
        # Can close any number of open brackets, open any number of new brackets, then choose any operation
        # Would seem like 4*4*4, but we limit total num of brackets to 3 and either open or close at each ind, not both
        bracketExpressions = [
            (curExpression + [self.cards[cardInd]], 0)
        ]
        for numToOpen in range(1, 4 - numBracketsUsed):
            bracketExpressions.append(
                (curExpression + ["("]*numToOpen + [self.cards[cardInd]], numToOpen)
            )
        
        for numToClose in range(1, numOpenBrackets + 1):
            bracketExpressions.append(
                (curExpression + [self.cards[cardInd]] + [")"]*numToClose, -numToClose)
            )

        for exprBeforeOp, deltaBrackets in bracketExpressions:
            for op in self.operations:
                expr = exprBeforeOp + [op]
                if self.exploreAllOptions(expr, numOpenBrackets + deltaBrackets, numBracketsUsed + max(0, deltaBrackets), cardInd + 1):
                    return True

        return False


    def judgePoint24(self, cards: List[int]) -> bool:
        # Exactly 4 cards. How hard is it to just bruteforce?
        # I didn't realize we can rearrange the numbers, but we optimized the function to be about 16^3, so we can just bruteforce it here too
        self.operations = ['+', '-', '*', '/']
        for cardsInOrder in itertools.permutations(cards):
            self.cards =  [str(e) for e in cardsInOrder]
            if self.exploreAllOptions([], 0, 0, 0):
                return True
        return False

        