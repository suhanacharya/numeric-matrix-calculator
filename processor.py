from matrix import Matrix

def read_matrix2D(m):
    matrix = []
    for x in range(m):
        row = input().split()
        row_integer = [float(num) for num in row]
        matrix.append(row_integer)

    return matrix


def read_order2D():
    order_of_matrix_1 = input().split(" ")

    return int(order_of_matrix_1[0]), int(order_of_matrix_1[1])


def print_matrix2D(matrix, m, n):
    for x in range(m):
        for y in range(n):
            print(round(matrix[x][y]), end=" ")
        print()


def show_menu():
    print("1. Add matrices\n2. Multiply matrix by a constant")
    print("3. Multiply matrices\n4. Transpose matrix\n0. Exit")
    print("Your choice: ", end="")
    choice = int(input())

    return choice


def add_matrices():
    print("Enter the order of first matrix: ", end=" ")
    m, n = read_order2D()
    matrix_1 = read_matrix2D(m)
    print("Enter the order of second matrix: ", end=" ")
    p, q = read_order2D()
    matrix_2 = read_matrix2D(p)
    if m == p and n == q:
        sum_matrix = [[matrix_1[x][y] + matrix_2[x][y] for y in range(q)]
                      for x in range(p)]
        print("The result is:")
        print_matrix2D(sum_matrix, m, n)
    else:
        print("The operation cannot be performed.")


def const_to_matrix():
    print("Enter the size of matrix: ", end=" ")
    m, n = read_order2D()
    print("Enter matrix: ")
    matrix = read_matrix2D(m)
    constant = float(input())
    c_matrix = [[matrix[x][y] * constant for y in range(n)]
                for x in range(m)]
    print("The result is:")
    print_matrix2D(c_matrix, m, n)


def matrix_multiply():
    print("Enter the order of first matrix: ", end=" ")
    m, n = read_order2D()
    print("Enter first matrix: ")
    matrix_1 = read_matrix2D(m)
    print("Enter the order of second matrix: ", end=" ")
    p, q = read_order2D()
    print("Enter second matrix: ")
    matrix_2 = read_matrix2D(p)
    if n == p:
        matrix_3 = [[0 for y in range(q)] for x in range(m)]
        # matrix_3 = [[[matrix_1[x][k]*matrix_2[k][y] + matrix_3[x][y]
        #              for k in range(q)] for y in range(m)]
        #             for x in range(m)]
        for x in range(m):
            for y in range(q):
                for k in range(p):
                    matrix_3[x][y] += matrix_1[x][k] * matrix_2[k][y]

        print("The result is:")
        print_matrix2D(matrix_3, m, q)
    else:
        print("The operation cannot be performed.")


def main_transpose():
    print("Enter matrix size: ", end=" ")
    m, n = read_order2D()
    print("Enter matrix: ")
    matrix = read_matrix2D(m)

    t_matrix = [[matrix[y][x] for y in range(n)] for x in range(m)]

    print_matrix2D(t_matrix, n, m)


def main():
    while True:
        choice = show_menu()

        if choice == 1:
            add_matrices()
        elif choice == 2:
            const_to_matrix()
        elif choice == 3:
            matrix_multiply()
        elif choice == 4:
            print("1. Main diagonal\n2. Side diagonal")
            print("3. Vertical line\n4. Horizontal line")
            ch = int(input())
            if ch == 1:
                main_transpose()
            elif ch == 2:
                pass
            elif ch == 3:
                pass
            elif ch == 4:
                pass
        elif choice == 0:
            break


if __name__ == "__main__":
    main()
