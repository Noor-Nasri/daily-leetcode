class RandomizedSet:

    def __init__(self):
        self.ind_pointers = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val in self.ind_pointers:
            return False
        
        self.ind_pointers[val] = len(self.data_list)
        self.data_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not (val in self.ind_pointers):
            return False
        
        ind_target = self.ind_pointers[val]
        ind_last = len(self.data_list) - 1

        if (ind_target == ind_last):
            self.data_list.pop()
        else:
            val_last = self.data_list[-1]
            self.data_list[ind_target] = val_last
            self.ind_pointers[val_last] = ind_target
            self.data_list.pop()
        
        del self.ind_pointers[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()