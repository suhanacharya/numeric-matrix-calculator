# Lesser NumPy!

### Initialization:
    import matrix
    my_matrix = Matrix()

matrix.py consists of a Matrix Class provides several functionality that are adopted from the real NumPy Library.

## These methods are:

<hr>

- #### Matrix.read_matrix()

        def read_matrix2D(self):
            """
            To read matrix from the console input to store in self.matrix
            Reads one row at a time and splits into array of floats
            """
            
    Usage:
    
         my_matrix.read_matrix()
 
<hr>

- #### Matrix.read_order()
        
        def read_order2D(self):
            """
            To take shape of matrix as a string and assign to self.shape list
            """
            
    Usage:
        
        my_matrix.read_order2D()
        
<hr>

- #### Matrix.print()

        def print(self, t=0):
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