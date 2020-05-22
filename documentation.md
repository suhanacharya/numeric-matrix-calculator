# Lesser NumPy!

### Initialization:
	import matrix
	my_matrix = Matrix()

matrix.py consists of a Matrix Class provides several functionality that are adopted from the real NumPy Library.

## These methods are:

<hr>

- #### Matrix.read_matrix()

			"""
			To read matrix from the console input to store in self.matrix
			Reads one row at a time and splits into array of floats
			"""
			
	Usage:
	
		 my_matrix.read_matrix()
 
<hr>

- #### Matrix.read_order()
		
			"""
			To take shape of matrix as a string and assign to self.shape list
			"""
			
	Usage:
		
		my_matrix.read_order2D()
		
<hr>

- #### Matrix.print()

		
		"""
			Printing matrix on console.
			Parameter:
			t - type of output
				default t = 0 which prints the matrix as a normal list.
				t = 1 prints the matrix with space and newline like a string
		"""
		
	Usage: Two ways to use the print() method.
	
	- To print matrix as a list form:
		
			my_matrix.print()
	- To print matrix as rows and columns with space and new-line:
	
			my_matrix.print(t=1)
		
<hr>

- #### Matrix.\_\_add__()
	
		"""
			Adds two objects of Matrix class and returns the sum matrix object.
			sum_matrix is the addition of matrix1 + matrix2

			Parameter:
				self - the first matrix object to be added
				other -
					- the other matrix object that has to be added
					- an integer or float to add component-wise

			returns:
				a matrix object whose self.matrix is the sum_matrix and self.shape is shape of added matrix
		"""
	Usage:
	
		my_matrix1 = Matrix()
		my_matrix2 = Matrix()
		
		my_matrix = my_matrix1 + my_matrix2
<hr>

- #### Matrix.\_\_sub__()

		"""
			Subtracts two objects of Matrix class and returns the difference matrix object.
            diff_matrix is the addition of matrix1 + matrix2

            Parameter:
                self - the first matrix object to be diff
                other -
                    - the other matrix object that has to be added
                    - an integer or float to add component-wise

            returns:
                a matrix object whose self.matrix is the diff_matrix and self.shape is shape of added matrix
        """
	Usage:
	    my_matrix1 = Matrix()
		my_matrix2 = Matrix()
		
		my_matrix = my_matrix1 - my_matrix2
	
- #### Matrix.\_\_mul__()

        """
            Supports two types of multiplication.
            Matrix to matrix multiplication using the matrix rules
            Matrix and constant multiplication to multiply a constant component wise.

            Parameters:
                self - the first matrix
                other - Either another matrix or a constant
                    if other is Matrix object, then it does matrix to matrix multiplication
                    if other is a float or an integer, it does matrix to constant multiplication
                multiplication_type -
                    matrix_multiplication - Indicates if the multiplication is using rules of matrix multiplication
                    component_wise - Indicates if the multiplication is done component_wise

            returns:
                the product matrix object after m to m multiplication.
                or
                the product matrix object after m to c multiplication.
        """
    
    Usage:
    
        my_matrix = my_matrix1 * my_matrix2
      
	