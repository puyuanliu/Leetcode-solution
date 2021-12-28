class Fancy:

    def __init__(self):
        self.storage_list = []
        self.x_factor_list = []  # List for multiplication track
        self.constant_list = []  # List for addition track
        self.current_x_factor = 1
        self.current_constant = 0
        self.storage = {}
        
    def append(self, val: int) -> None:
        self.storage_list.append(val)
        self.x_factor_list.append(self.current_x_factor)
        self.constant_list.append(self.current_constant)

    def addAll(self, inc: int) -> None:
        self.current_constant += inc
        self.current_constant = self.current_constant
        self.storage = {}

    def multAll(self, m: int) -> None:
        self.current_constant *= m
        self.current_x_factor *= m
        self.current_constant %= (10**9 + 7)
        self.storage = {}

    def getIndex(self, idx: int) -> int:
        if idx in self.storage.keys():
            return self.storage[idx]
        if idx >= len(self.storage_list):
            return -1
        else:
            result = self.storage_list[idx]  # initialize
            diff_x_factor = self.current_x_factor // self.x_factor_list[idx]
            diff_constant = self.current_constant - diff_x_factor*self.constant_list[idx]
            diff_constant %= (10**9 + 7)
            result = diff_x_factor * result + diff_constant
            final_result = (result) % (10**9 + 7)
            self.storage[idx] = final_result
            return final_result
        
