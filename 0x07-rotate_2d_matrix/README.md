rotate_2d_matrix

Reversing and Transposing:

reversed(matrix) reverses the rows of the matrix.
zip(*reversed(matrix)) transposes the reversed matrix. This works because zip(*matrix) effectively transposes matrix.
List Comprehension:

[list(row) for row in ziped] converts each tuple in ziped (which represents a transposed row from the original matrix) into a list and collects them into a new list. This new list is then assigned back to matrix.
