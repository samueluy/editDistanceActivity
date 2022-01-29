"""
* @brief Finds the edit distance given two strings
* @param string1: String to be replaced
* @param string2: String to replace with
* @param i: Length of first string
* @param j: Length of second string

* @return Total weight of moves
"""

def findEditDistance(string1, string2, i, j):
    # Base case - String 1 is empty
    if i == len(string1):
        return j

    # Base case - String 2 is empty
    if j == len(string2):
        return i

    # If both characters are similar, do not add to the weight
    # Copy = 0
    if string1[i] == string2[j]:
        print("Copy", string1[i])
        return findEditDistance(string1, string2, i + 1, j + 1)

    # Increment weight then check for the minimum of the next characters
    return 1 + min(findEditDistance(string1, string2, i, j + 1),
                   findEditDistance(string1, string2, i + 1, j),
                   findEditDistance(string1, string2, i + 1, j + 1))

def insert(string1, string2, i, j):
    
    return 0

def remove(string1, string2, i, j):
    return 0

def replace(string1, string2, i, j):
    return 0

# Driver
string1 = "intention"
string2 = "execution"
print(findEditDistance(string1, string2, 0, 0))

"""
References:
- https://www.youtube.com/watch?v=XYi2-LPrwm4
- https://www.geeksforgeeks.org/edit-distance-dp-5/
"""
