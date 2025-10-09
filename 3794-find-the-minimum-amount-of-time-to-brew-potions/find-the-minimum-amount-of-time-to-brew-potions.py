class Solution:
    # So essentially, we need to know how long to wait before sending each potion down the line
    # I spent a lot of time working on some double binary search approach that didn't work.
    # We send potion 0 at time 0: then we have a time for each wizard being free.
    # Then for potion 1, we can go through the wizards and determine the delay each of them require. Max required delay is our delay
    # This is n*m which should pass, hopefully.

    def getBestDelayBetweenPotions(self, prevPotionCost, curPotionCost):
        totalWizardCost = 0
        maxDelayRequired = 0
        for wizardSkill in self.skill:
            finishTimePrevPotion = (totalWizardCost + wizardSkill) * prevPotionCost
            startTimeCurPotion = totalWizardCost*curPotionCost
            maxDelayRequired = max(maxDelayRequired, finishTimePrevPotion - startTimeCurPotion)
            totalWizardCost += wizardSkill
        return maxDelayRequired

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        self.skill = skill
        curTime = 0
        for potion_ind in range(1, len(mana)):
            curTime += self.getBestDelayBetweenPotions(mana[potion_ind - 1],  mana[potion_ind])

        return curTime + sum(skill)*mana[-1]

        