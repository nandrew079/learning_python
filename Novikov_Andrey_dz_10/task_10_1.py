class Matrix:
    def __init__(self, matrix):
        self.__len_str = 0
        try:
            len_str = len(matrix[0])
        except IndexError:
            print('Вы передали не матрицу')

        for m_str in matrix:
            if len(m_str) != len_str:
                raise ValueError('Некорректная матрица')

        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for m_str in self.matrix:
            for i in m_str:
                str_matrix = f'{str_matrix} {i}'
            str_matrix += '\n'

        return str_matrix

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append(list(map(sum, zip(self.matrix[i], other.matrix[i]))))
        return Matrix(new_matrix)


matrix_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix_c = matrix_a + matrix_b
print(matrix_a)
print(matrix_b)
print(matrix_c)
