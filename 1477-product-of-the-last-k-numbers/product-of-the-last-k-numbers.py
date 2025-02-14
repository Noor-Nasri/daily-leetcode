class ProductOfNumbers:
    def __init__(self):
        self.products = [1]
        self.numZeros = [0]
        self.curProd = 1
        self.numZero = 0


    def add(self, num: int) -> None:
        if num == 0:
            self.numZero += 1
        else:
            self.curProd *= num

        self.products.append(self.curProd)
        self.numZeros.append(self.numZero)


    def getProduct(self, k: int) -> int:
        if self.numZero > self.numZeros[-k - 1]:
            return 0
        return self.curProd//self.products[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)