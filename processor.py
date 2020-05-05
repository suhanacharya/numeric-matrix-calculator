from matrix import Matrix


def show_menu():
    print("1. Add matrices\n2. Multiply matrix by a constant")
    print("3. Multiply matrices\n4. Transpose matrix\n0. Exit")
    print("Your choice: ", end="")
    choice = int(input())

    return choice


def main():
    while True:
        choice = show_menu()

        if choice == 1:
            matrix_1 = Matrix()
            print("Enter the order of first matrix: ", end=" ")
            matrix_1.read_order2D()
            matrix_1.read_matrix2D()

            matrix_2 = Matrix()
            print("Enter the order of second matrix: ", end=" ")
            matrix_2.read_order2D()
            matrix_2.read_matrix2D()

            matrix_3 = matrix_1 + matrix_2
            print("The result is: ")
            matrix_3.print(t=1)

        elif choice == 2:
            matrix_1 = Matrix()
            print("Enter the order of first matrix: ", end=" ")
            matrix_1.read_order2D()
            matrix_1.read_matrix2D()
            constant = round(float(input()))
            matrix_2 = matrix_1 * constant
            print("The result is:")
            matrix_2.print(t=1)

        elif choice == 3:
            matrix_1 = Matrix()
            print("Enter the order of first matrix: ", end=" ")
            matrix_1.read_order2D()
            matrix_1.read_matrix2D()

            matrix_2 = Matrix()
            print("Enter the order of second matrix: ", end=" ")
            matrix_2.read_order2D()
            matrix_2.read_matrix2D()

            matrix_3 = matrix_1 * matrix_2

            if matrix_3 != -1:
                print("The result is: ")
                matrix_3.print(t=1)

        elif choice == 4:
            print("1. Main diagonal\n2. Side diagonal")
            print("3. Vertical line\n4. Horizontal line")
            ch = int(input())

            matrix_1 = Matrix()
            print("Enter the matrix size: ", end=" ")
            matrix_1.read_order2D()
            print("Enter the matrix:")
            matrix_1.read_matrix2D()

            if ch == 1:
                matrix_2 = Matrix()
                matrix_2 = matrix_1.main_transpose()
                print("The result is: ")
                matrix_2.print(t=1)
            elif ch == 2:
                matrix_2 = Matrix()
                matrix_2 = matrix_1.side_transpose()
                print("The result is: ")
                matrix_2.print(t=1)
            elif ch == 3:
                matrix_2 = Matrix()
                matrix_2 = matrix_1.vertical_transpose()
                print("The result is: ")
                matrix_2.print(t=1)
            elif ch == 4:
                matrix_2 = Matrix()
                matrix_2 = matrix_1.horizontal_transpose()
                print("The result is: ")
                matrix_2.print(t=1)

        elif choice == 0:
            break


if __name__ == "__main__":
    main()
