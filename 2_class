class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        self.lst += a
        while len(self.lst) >= 5:

            print(sum(self.lst[:5]))
            self.lst = self.lst[5:]

    def get_current_part(self):
        return self.lst

#вариант 2

class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
