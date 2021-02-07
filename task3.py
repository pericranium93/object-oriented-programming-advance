class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return self.nucleus + other.nucleus

    def __sub__(self, other):
        if other.nucleus >= self.nucleus:
            return 'Количество ячеек должно быть меньше, чем у первой клетки'
        else:
            return self.nucleus - other.nucleus

    def __mul__(self, other):
        return self.nucleus * other.nucleus

    def __truediv__(self, other):
        return round(self.nucleus / other.nucleus)

    def make_order(self, nucleus_in_row):
        line = str(nucleus_in_row * '*')
        list_of_lines = []
        i = 0
        while i < self.nucleus // nucleus_in_row:
            list_of_lines.append(line)
            i += 1
        nl = '\n'
        return f'{nl.join(list_of_lines)}\n{self.nucleus % 5 * "*"}'
    # не получилось сделать с for, посмотрел разбор, узнал о магическом "_" но свое решение оставил.


a = Cell(50)
b = Cell(26)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b.make_order(5))

