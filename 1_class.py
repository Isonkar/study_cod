class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.coin = 0

    def can_add(self, v):
        if v > self.capacity or v > self.capacity - self.coin:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.coin += v   
