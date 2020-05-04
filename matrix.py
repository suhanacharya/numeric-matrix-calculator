class Matrix:

    def __init__(self, size=[1, 1]):
        self.matrix = None
        self.size = size
        pass

    def read_matrix2D(self,):
        self.matrix = []
        for x in range(self.size[0]):
            row = input().split()
            row_integer = [float(num) for num in row]
            self.matrix.append(row_integer)

    def read_order2D(self):
        order = input().split(" ")
        self.size = [int(order[0]), int(order[1])]

    def print(self, t=0):
        if t == 0:
            print(self.matrix)
        elif t == 1:
            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    print(round(self.matrix[x][y]), end=" ")
                print()

    def __add__(self, other):
        if self.size[0] == other.size[0] and self.size[1] == other.size[1]:
            sum_matrix = [[self.matrix[x][y] + other.matrix[x][y]
                           for y in range(self.size[1])]
                          for x in range(self.size[0])]
            new_matrix = Matrix(size=[self.size[0], self.size[1]])
            new_matrix.matrix = sum_matrix
            return new_matrix
        else:
            print("The operation cannot be performed.")

        return self

    def __mul__(self, other):
        if type(other) == type(self):
            if self.size[1] == other.size[0]:
                p_matrix = [[0 for y in range(other.size[1])] for x in range(self.size[0])]
                for x in range(self.size[0]):
                    for y in range(other.size[1]):
                        for k in range(other.size[0]):
                            p_matrix[x][y] += self.matrix[x][k] * other.matrix[k][y]
                new_matrix = Matrix(size=[self.size[0], other.size[1]])
                new_matrix.matrix = p_matrix
                return new_matrix
            else:
                print("The operation cannot be performed")
            return self

        else:
            c_matrix = [[round(self.matrix[x][y] * other) for y in range(self.size[1])]
                        for x in range(self.size[0])]
            new_matrix = Matrix(size=[self.size[0], self.size[1]])
            new_matrix.matrix = c_matrix
            return new_matrix

    def main_transpose(self):
        t_matrix = [[self.matrix[y][x] for y in range(self.size[1])] for x in range(self.size[0])]
        new_matrix = Matrix(size=[self.size[1], self.size[0]])
        new_matrix.matrix = t_matrix
        return new_matrix

