"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-11"
-------------------------------------------------------
"""
# Imports

# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    v = 0
    while v < len(values):
        v2 = v + 1
        while v2 < len(values):
            if values[v] == values[v2]:
                values.pop(v2)
            else:
                v2 += 1
        v += 1

    return None


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    s = 0
    while s < len(subtrahend):
        m = 0
        while m < len(minuend):
            if minuend[m] == subtrahend[s]:
                minuend.pop(m)
            else:
                m += 1
        s += 1

    return None


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = fv.readline()
    upp = 0
    low = 0
    dig = 0
    whi = 0
    rem = 0

    while line != "":
        for c in line:
            if c.isdigit():
                dig += 1
            elif c.isupper():
                upp += 1
            elif c.islower():
                low += 1
            elif c.isspace():
                whi += 1
            else:
                rem += 1
        line = fv.readline()

    return upp, low, dig, whi, rem


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right. Already used characters are ignored.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    c = 0
    length = len(string) - len(sub)

    while c < length:
        if string[c:c + len(sub)] == sub:
            locations.append(c)
            c += len(sub)
        else:
            c += 1
    return locations


def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = False
    compare_forward = ""
    compare_backwards = ""

    for c in string:
        if c.isalnum():
            compare_forward = compare_forward + c.upper()

    for c in compare_forward[::-1]:
        compare_backwards = compare_backwards + c

    if compare_forward == compare_backwards:
        palindrome = True

    return palindrome


def median_scores(fv):
    """
    -------------------------------------------------------
    Determines the median of a series of integers in a file.
    Use: median = median_scores(fv)
    -------------------------------------------------------
    Parameters:
        fv - a file variable for an already open file of integers (file)
    Returns:
        median - the median of the values in the file (float)
    -------------------------------------------------------
    """
    median = 0
    line = fv.readline()
    numList = []
    while line != "":
        line.strip()
        numList.append(int(line))
        line = fv.readline()
    numList.sort()
    pos = len(numList)
    if pos % 2 == 0:
        half = pos/2
        median = (numList[half-1] + numList[half])/2
    else:
        half = (pos/2) - 0.5
        median = numList[int(half)]

    return median


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []

    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        b.append(row)

    return b


def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []

    for row in a:
        for col in row:
            b.append(col)

    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    c = []

    rowsA = len(a)
    rowsB = len(b)
    colsB = len(b[0])

    if rowsA != colsB:
        print("Error, cannot multiply matrix.")
    else:
        for i in range(rowsA):
            row = []
            for j in range(colsB):
                row.append(0)
            c.append(row)

        for rA in range(rowsA):
            for cB in range(colsB):
                for rB in range(rowsB):
                    c[rA][cB] += a[rA][rB] * b[rB][cB]

    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = []

    for col in range(len(a[0])):
        rows = []
        for row in range(len(a)):
            rows.append(a[row][col])
        rows.reverse()
        b.append(rows)

    return b
