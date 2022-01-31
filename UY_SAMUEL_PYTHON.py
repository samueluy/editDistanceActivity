import array
import copy

"""
********************
Name: Uy, Samuel Jedidiah A.
Language: Python
Paradigm: Functional
********************
"""


def findEditDistance(str1, str2, i, j):
    """ Finds the edit distance given two strings
    Parameters
    ----------
    str1 : str
        String to be replaced
    str2 : str
        String to replace with
    i : int
        Length of first string
    j : int
        Length of second string
    """
    print("Input string 1 = " + str1)
    print("Input string 2 = " + str2)

    typedef_matrix = []  # Initialize empty list
    row_matrix = createListRow(typedef_matrix, 0, len(str1) + 1)  # Initialize the row values of the list
    initialized_matrix = createListCol(row_matrix, 0, len(str1) + 1, len(str2) + 1)  # Initialize the column values of
    # the list
    initialized_matrix_copy = copy.deepcopy(initialized_matrix)
    bottom_set_matrix = setBaseValues(initialized_matrix_copy, i, j, 0)  # Set the bottom values of the list
    bottom_set_matrix_copy = copy.deepcopy(bottom_set_matrix)
    matrix = setBaseValues(bottom_set_matrix_copy, i, j, 0)  # Set the side values of the list

    recur_i(0, j, i + 1, j + 1, matrix, str1, str2)  # Run the recursive code to create the matrix

    # Remove "#" -> Can be used to print the matrix to aid with visualization
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

    print("Edit Distance:", matrix[i][j])  # Print the Levenshtein Distance of the given strings
    print("Operations:")
    results = []  # Initialize list for results
    matrixBacktrack(matrix, str1, str2, len(str1), len(str2), results)  # Backtrack and place the steps to results
    results.reverse()  # Reverse the results list
    printList(results, len(results) - 1, 0)  # Print the steps to achieve the minimum edit distance of two strings


def createListRow(matrix, n, length):
    """ Creates empty lists inside a given list
    Parameters
    ----------
    matrix : list
        List that will be modified
    n : int
        Current iteration
    length : int
        Length of the list

    Return
    ------
    matrix : list
        modified matrix
    """
    if n < length:
        matrix.append([])  # Add empty lists
        createListRow(matrix, n + 1, length)
        return matrix


def createListCol(matrix, n, length, rowLength):
    """ Adds the zeroes inside all the lists in the given matrix
    Parameters
    ----------
    matrix : list
        List that will be modified
    n : int
        Current iteration
    length : int
        Column length of the list
    rowLength : int
        Length of the row

    Return
    ------
    matrix : list
        modified matrix
    """
    if n < length:
        zeroListRow(matrix[n], 0, rowLength)  # Adds the zeroes
        createListCol(matrix, n + 1, length, rowLength)
        return matrix


def zeroListRow(matrix, n, length):
    """ Adds zeroes inside a given list
    Parameters
    ----------
    matrix : list
        List that will be modified
    n : int
        Current iteration
    length : int
        Number of zeroes to be added

    Return
    ------
    matrix : list
        modified matrix
    """
    if n < length:
        matrix.append(0)
        zeroListRow(matrix, n + 1, length)
        return matrix


def setBaseValues(matrix, len1, len2, i):
    """ Adds zeroes inside a given list
    Parameters
    ----------
    matrix : list
        List that will be modified
    len1 : int
        Length of first string
    len2 : int
        Length of second string
    i : int
        Current iteration

    Return
    ------
    matrix : list
        modified matrix
    """
    if i == len2:
        matrix[len1][i] = len2 - i
        return matrix

    matrix[len1][i] = len2 - i
    matrix = setBaseValues(matrix, len1, len2, i + 1)
    return matrix


def matrixBacktrack(matrix, str1, str2, i, j, results):
    """ Recursively backtracks through a given matrix to find the path of the smallest edit distance
     Parameters
     ----------
     matrix : list
         List that will be modified
     str1 : str
        First string
     str2 : str
        Second string
     i : int
         Length of first string
     j : int
         Length of second string
     results : list
         List that contains the weighted steps to the end of the matrix

     Return
     ------
     int
         Value on the current index of matrix
     """
    if i == 0 and j == 0:
        return matrix[0][0]
    elif i == 0:
        return matrix[0][j]
    elif j == 0:
        return matrix[i][0]

    insert = matrix[i][j - 1]  # Sets the value for insert
    remove = matrix[i - 1][j]  # Sets the value for remove
    replace = matrix[i - 1][j - 1]  # Sets the value for replace
    minimum = min(insert, remove, replace)  # Get the minimum value between insert, remove, and replace

    if minimum == replace and matrix[i][j] == matrix[i - 1][j - 1]:  # If same values, copy
        return matrixBacktrack(matrix, str1, str2, i - 1, j - 1, results)
    elif minimum == replace:  # Diagonal
        results.append("Replace " + str1[i - 1] + " with " + str2[j - 1])
        return matrixBacktrack(matrix, str1, str2, i - 1, j - 1, results)

    elif minimum == insert:  # Up
        results.append("Insert " + str2[j - 1])
        return matrixBacktrack(matrix, str1, str2, i, j - 1, results)

    elif minimum == remove:  # Left
        results.append("Remove " + str1[j - 1])
        return matrixBacktrack(matrix, str2, str2, i - 1, j, results)


def printList(results, size, i):
    """ Prints the contents of a given list
    Parameters
    ----------
    results : list
        List to be printed
    size : int
        Number of elements in the list
    i : int
        Current iteration

    Return
    ------
    int
        Default terminating value
    """
    if i == size:
        print(results[i])
        return 0

    print(results[i])
    printList(results, size, i + 1)
    return 0


def recur_i(i, j, i_size, j_size, matrix, str1, str2):
    """ Recursively run recur_j i_size times
    Parameters
    ----------
    i : int
        Current iteration of i
    j : int
        Current iteration of j
    i_size : int
        Limit of i
    j_size : int
        Limit of j
    matrix : list
        Matrix to be modified
    str1: str
        First input string
    str2 : str
        Second input string

    Return
    ------
    new_matrix : list
        Modified matrix
    """
    if i < i_size:
        recur_j(i, 0, j_size, matrix, str1, str2)
        new_matrix = recur_i(i + 1, j, i_size, j_size, matrix, str1, str2)
        return new_matrix


def recur_j(i, j, size, matrix, str1, str2):
    """ Recursively run recur_j i_size times
    Parameters
    ----------
    i : int
        Current iteration of i
    j : int
        Current iteration of j
    size : int
        Limit of j
    matrix : list
        Matrix to be modified
    str1: str
        First input string
    str2 : str
        Second input string

    Return
    ------
    list
        Modified matrix
    """
    if j < size:

        # Insert remaining characters for second string
        if i == 0:
            matrix[i][j] = j

        # Insert remaining characters for first string
        elif j == 0:
            matrix[i][j] = i

        # Similar characters are ignored
        elif str1[i - 1] == str2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1]

        #  Add 1 to the weight then find the minimum of the next sequence
        else:
            matrix[i][j] = 1 + min(matrix[i][j - 1],  # Insert
                                   matrix[i - 1][j],  # Remove
                                   matrix[i - 1][j - 1])  # Replace

        return recur_j(i, j + 1, size, matrix, str1, str2)


# Driver
string1 = input("Input string 1 = ")
string2 = input("Input string 2 = ")
# string1 = "intention"
# string2 = "execution"
findEditDistance(string1, string2, len(string1), len(string2))

"""
References:
- https://www.youtube.com/watch?v=XYi2-LPrwm4
- https://www.geeksforgeeks.org/edit-distance-dp-5/
"""
