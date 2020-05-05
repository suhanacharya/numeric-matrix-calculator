class Matrix:

    def __init__(self, size=[1, 1]):
        self.matrix = None
        self.size = size
        pass

    def read_matrix2D(self):
        """
        To read matrix from the console input to store in self.matrix
        Reads one row at a time and splits into array of floats
        """
        self.matrix = []
        for x in range(self.size[0]):
            row = input().split()
            row_integer = [round(float(num)) for num in row]
            self.matrix.append(row_integer)

    def read_order2D(self):
        """
        To take size of matrix as a string and assign to self.size list
        """
        order = input().split(" ")
        self.size = [int(order[0]), int(order[1])]

    def print(self, t=0):
        """
            Printing matrix on console.
            Parameter:
            t - type of output
                default t = 0 which prints the matrix as a normal list.
                t = 1 prints the matrix with space and newline like a string
        """
        if t == 0:
            print(self.matrix)
        elif t == 1:
            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    print(round(self.matrix[x][y]), end=" ")
                print()

    def __add__(self, other):
        """
            Adds two objects of Matrix class and returns the sum matrix object.
            sum_matrix is the addition of matrix1 + matrix2

            Parameter:
                self - the first matrix object to be added
                other - the other matrix object that has to be added

            returns:
                a matrix object whose self.matrix is the sum_matrix and self.size is size of added matrix
        """
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
        """
            Supports two types of multiplication.
            Matrix to matrix multiplication using the matrix rules
            Matrix and constant multiplication to multiply a constant component wise.

            Parameters:
                self - the first matrix
                other - Either another matrix or a constant
                    if other is Matrix object, then it does matrix to matrix multiplication
                    if other is a float or an integer, it does matrix to constant multiplication

            returns:
                the product matrix object after m to m multiplication
                or
                the product matrix object after m to c multiplication
        """
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
        """
            To transpose the self.matrix over its main diagonal

            returns:
                A Matrix object that is the transpose about its main diagonal.
        """
        t_matrix = [[self.matrix[y][x] for y in range(self.size[1])] for x in range(self.size[0])]
        new_matrix = Matrix(size=[self.size[1], self.size[0]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def side_transpose(self):
        """
            To transpose matrix over its secondary/ side diagonal

            returns:
                A matrix object that is transpose about its side diagonal
        """
        t_matrix = []
        counter_row = 0
        for i in reversed(range(self.size[0])):
            t_matrix.append([])
            for j in reversed(range(self.size[1])):
                t_matrix[counter_row].append(self.matrix[j][i])
            counter_row += 1

        new_matrix = Matrix(size=[self.size[1], self.size[0]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def vertical_transpose(self):
        """
            To transpose the matrix over its 'vertical axis'

            returns:
                A matrix object that is reversed about its rows

            Usage:
                Example:
                    If                              After vertical transpose,
                       matrix = [[1, 2, 3],         The matrix = [[3, 2, 1],
                                 [4, 5, 6],                       [6, 5, 4],
                                 [7, 8, 9]]                       [9, 8, 7]]
        """
        t_matrix = []
        for i in range(self.size[0]):
            t_matrix.append(list(reversed(self.matrix[i])))

        new_matrix = Matrix(size=[self.size[0], self.size[1]])
        new_matrix.matrix = t_matrix
        return new_matrix

    def horizontal_transpose(self):
        """
            To transpose the matrix over its 'horizontal axis'

            returns:
                A matrix object that is reversed about its columns

            Usage:
                Example:
                    If                              After Horizontal transpose,
                       matrix = [[1, 2, 3],         The matrix = [[7, 8, 9],
                                 [4, 5, 6],                       [4, 5, 6],
                                 [7, 8, 9]]                       [1, 2, 3]]
        """
        t_matrix = []

        for i in range(self.size[0]):
            t_matrix.append([])
            for j in range(self.size[1]):
                t_matrix[i].append(self.matrix[self.size[0] - 1 - i][j])

        new_matrix = Matrix(size=[self.size[0], self.size[1]])
        new_matrix.matrix = t_matrix
        return new_matrix
