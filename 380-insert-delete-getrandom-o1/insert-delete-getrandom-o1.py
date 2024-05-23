class RandomizedSet:

    def __init__(self):
        self.data_set = set()
        self.data_list = list()

    def insert(self, val: int) -> bool:
        if val in self.data_set:
            return False
        
        self.data_set.add(val)
        self.data_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not (val in self.data_set):
            return False
        

        self.data_set.remove(val)
        self.data_list.remove(val)
        return True
        

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.data_list)-1)
        return self.data_list[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()