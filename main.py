import array

"""
* @brief Finds the edit distance given two strings
* @param string1: String to be replaced
* @param string2: String to replace with
* @param i: Length of first string
* @param j: Length of second string

* @return Total weight of moves
"""

import copy


def findEditDistance(str1, str2, i, j):
    print("Input string 1 = " + str1)
    print("Input string 2 = " + str2)
    initialized_matrix = [[0] * (j + 1) for x in range(i + 1)]
    initialized_matrix_copy = copy.deepcopy(initialized_matrix)  # Deep copy of initialized matrix
    bottom_set_matrix = setBottomBaseValues(initialized_matrix_copy, i, j, 0)  # Matrix with bottom values
    bottom_set_matrix_copy = copy.deepcopy(bottom_set_matrix)  # Deep copy of matrix with bottom values
    matrix = setSideBaseValues(bottom_set_matrix_copy, i, j, 0)  # Matrix with base values

    print("base", i)
    recur_i(0, j, i + 1, matrix, str1, str2)

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    print("Edit Distance:", matrix[i][j])
    print("Operations:")
    results = []  # Initialize list for results
    matrixBacktrack(matrix, str1, str2, len(str1), len(str2), results)
    results.reverse()  # Reverse the results list
    printList(results, len(results) - 1, 0)


def setBottomBaseValues(matrix, len1, len2, i):
    if i == len2:
        matrix[len1][i] = len2 - i
        return matrix

    matrix[len1][i] = len2 - i
    matrix = setBottomBaseValues(matrix, len1, len2, i + 1)
    return matrix


def setSideBaseValues(matrix, len1, len2, i):
    if i == len1:
        matrix[i][len2] = len1 - i
        return matrix

    matrix[i][len2] = len1 - i
    matrix = setSideBaseValues(matrix, len1, len2, i + 1)
    return matrix


def matrixBacktrack(matrix, str1, str2, i, j, results):
    if i == 0 and j == 0:
        return matrix[0][0]
    elif i == 0:
        return matrix[0][j]
    elif j == 0:
        return matrix[i][0]

    insert = matrix[i][j - 1]
    remove = matrix[i - 1][j]
    replace = matrix[i - 1][j - 1]
    minimum = min(insert, remove, replace)

    if minimum == replace and matrix[i][j] == matrix[i - 1][j - 1]:  # same values, copy
        return matrixBacktrack(matrix, str1, str2, i - 1, j - 1, results)
    elif minimum == replace:
        results.append("Replace " + str1[i - 1] + " with " + str2[j - 1])
        return matrixBacktrack(matrix, str1, str2, i - 1, j - 1, results)

    elif minimum == insert:
        results.append("Insert " + str2[j - 1])
        return matrixBacktrack(matrix, str1, str2, i, j - 1, results)

    elif minimum == remove:
        results.append("Remove " + str1[j - 1])
        return matrixBacktrack(matrix, str2, str2, i - 1, j, results)


def printList(results, size, i):
    if i == size:
        print(results[i])
        return 0

    print(results[i])
    printList(results, size, i + 1)
    return 0


def recur_i(i, j, size, matrix, str1, str2):
    if i < size:
        for j in range(j + 1):
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                matrix[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                matrix[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1],  # Insert
                                       matrix[i - 1][j],  # Remove
                                       matrix[i - 1][j - 1])  # Replace

        new_matrix = recur_i(i + 1, j, size, matrix, str1, str2)
        return new_matrix


# Driver
# string1 = input("Input string 1 = ")
# string2 = input("Input string 2 = ")
string1 = "food"
string2 = "money"
findEditDistance(string1, string2, len(string1), len(string2))

"""
References:
- https://www.youtube.com/watch?v=XYi2-LPrwm4
- https://www.geeksforgeeks.org/edit-distance-dp-5/
"""
