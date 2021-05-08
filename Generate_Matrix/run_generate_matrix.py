def generate_matrix(size):
    mat = []
    for i in range(size):
        a = []
        for j in range(size):
            a.append(0)
        mat.append(a)
    return mat


def edit_diagonal(matrix, character):
    for i in range(len(matrix[0])):
        matrix[i][i] = character
    return matrix


def show_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=' ')
        print()  # this prints by default a new line


def __main__():
    mat_size = int(input("Enter size of the matrix: "))
    diagonal_character = input("Enter diagonal character: ")
    my_matrix = generate_matrix(mat_size)
    my_matrix = edit_diagonal(my_matrix, diagonal_character)
    show_matrix(my_matrix)


__main__()
