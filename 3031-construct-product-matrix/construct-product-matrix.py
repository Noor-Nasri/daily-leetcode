class Solution:
    # Seems like a simple product(all) / val for each val, except modulo breaks
    # How can we do this without division? We can do prod(before)*prod(after)

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prodBeforeInd = [1]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                nextProd = (prodBeforeInd[-1] * grid[row][col]) % (12345)
                prodBeforeInd.append(nextProd)

        prodFromInd = [1]
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) -1, -1, -1):
                nextProd = (prodFromInd[-1] * grid[row][col]) % (12345)
                prodFromInd.append(nextProd)
        prodFromInd = prodFromInd[::-1]

        counter = 0
        finalArr = []
        for row in range(len(grid)):
            newRow = []
            for col in range(len(grid[0])):
                prod = (prodBeforeInd[counter] * prodFromInd[counter + 1]) % 12345
                newRow.append(prod)
                counter += 1
            finalArr.append(newRow)
        
        return finalArr
