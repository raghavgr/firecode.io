""" Check if string is a Palindrome """
def is_palindrome(input_string):
    """
    Compare ith character with the furthest minus i characters in the given string.
    """
    for i in range(len(input_string)/2):
        if input_string[i] != input_string[len(input_string) - i - 1]:
            return False
    return True
