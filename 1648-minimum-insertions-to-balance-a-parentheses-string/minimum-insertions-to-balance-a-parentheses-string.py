class Solution:
    # Seems like a simple sweep, if there's too many ), we must add a ( before them.
    # At the end, we close all the unclosed brackets.

    def minInsertions(self, s: str) -> int:
        numExpectedClosures = 0
        numChanges = 0
        expectingSecondClose = False

        for c in s:
            if c == "(":
                if expectingSecondClose:
                    # Before we can open this, we need to add a second )
                    expectingSecondClose = False
                    numExpectedClosures -= 1
                    numChanges += 1

                numExpectedClosures += 2
            elif numExpectedClosures:
                numExpectedClosures -= 1
                expectingSecondClose = not expectingSecondClose

            else:
                # Forced to add an open bracket for this one
                numChanges += 1
                numExpectedClosures += 1
                expectingSecondClose = True
        

        return numChanges + numExpectedClosures