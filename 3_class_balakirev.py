class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0): #поименованные аргументы со значением по умолчанию
        self.x = x
        self.y = y

    def set_coords(self, x, y): #создает локальные атрибуты для экземпляра класса
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point(20, 40) # если указать аргументы, значения присвоятся, если нет - значения по умолчанию 
print((pt.__dict__))
