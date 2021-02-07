class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        a = ''
        for el in self.list:
            a += '  '.join(str(i) for i in el) + '\n'
        return a

    def __add__(self, other):
        new_list = []
        # a = ''  # если используем return a
        if len(self.list) == len(other.list):
            for i, j in zip(self.list, other.list):
                if len(i) == len(j):
                    sum_of_element = [el1 + el2 for el1, el2 in zip(i, j)]
                    new_list.append(sum_of_element)
                else:
                    return 'Матрицы разного размера'
        else:
            return 'Матрицы разного размера'
        # for my_list in c:
        #     a += '  '.join((str(num) for num in my_list)) + '\n'
        return Matrix(new_list)  # return a


list = Matrix([[2, 5, 6], [25, 3, -5], [0, 356, 23]])
a = Matrix([[6, 8, -19], [4, 39, 74], [3, 5, 2]])
b = Matrix([[22, -5, 7], [6, 3, -1], [0, 7, 0]])
print(list)
c = a + b
print(a + b)
print(c)
# c = Matrix(a + b)  # в этом случае необходимо вернуть просто списко new_list
# print(c)
