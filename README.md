# Edit Distance Calculation

This Python code calculates the edit distance between two strings using the Levenshtein distance algorithm. The edit distance is the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another.

A Dynamic programming approach to find the minimum edit distance of two strings.

Functional programming paradigm.

## Code Details

```python
import array
import copy

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

    # Rest of the code...

# Rest of the code...

# Driver
string1 = "intention"
string2 = "execution"
findEditDistance(string1, string2, len(string1), len(string2))

"""
References:
- [YouTube Video](https://www.youtube.com/watch?v=XYi2-LPrwm4)
- [GeeksforGeeks Article](https://www.geeksforgeeks.org/edit-distance-dp-5/)
"""
