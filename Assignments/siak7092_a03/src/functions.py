"""
-------------------------------------------------------
Funtions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2025-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
OPERATORS = "+-*/"


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 0

    while source.is_empty() == False:
        if i % 2 == 0:
            target1.push(source.pop())
        else:
            target2.push(source.pop())

        i = i + 1

    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    holder = []

    while source.is_empty() == False:
        holder.append(source.pop())

    j = 0
    length = len(holder)

    while j < length:
        source.push(holder.pop())
        j = j + 1

    return None


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = False
    s1 = Stack()

    for c in string:
        if c.isalpha():
            s1.push(c)

    string1 = ""
    string2 = ""

    while s1.is_empty() == False:
        string1 += str(s1.pop()).lower()

    for c in string1[::-1]:
        string2 += c

    if string1 == string2:
        palindrome = True

    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    answer = 0
    s1 = Stack()
    equation = string.split()

    for eq in equation:
        if not (eq in OPERATORS):
            s1.push(eq)
        else:
            num1 = float(s1.pop())
            num2 = float(s1.pop())

            if eq == "+":
                s1.push(num2 + num1)
            elif eq == "-":
                s1.push(num2 - num1)
            elif eq == "*":
                s1.push(num2 * num1)
            else:
                s1.push(num2 / num1)

    answer = s1.pop()

    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    values_out = []
    s1 = Stack()

    for o in opstring:
        if o == "S":
            s1.push(values_in.pop(0))
        elif o == "X":
            values_out.append(s1.pop())

    if s1.is_empty() == False or len(values_in) > 0:
        values_out = None

    return values_out
