# Determine if a tuple can be made into a palindrome by removing exactly one element

# An example import. Delete or replace as desired. Be careful with what libraries you use:
# Non-default python libraries may not work in Zybooks.
import math 

# Subroutines if any, go here

# Fill in find_palindrome

def find_palindrome(pattern):
    """Find a palindrome tuple by removing exactly one element."""
    if not isinstance(pattern, tuple) or len(pattern) < 3:
        return None

    def is_palindrome(t):
        return t == t[::-1]

    def check_remove(left, right):
        """Check if removing the element at 'left' or 'right' results in a palindrome."""
        if is_palindrome(pattern[left + 1:right + 1]):
            return pattern[left + 1:right + 1]
        if is_palindrome(pattern[left:right]):
            return pattern[left:right]
        return None

    left, right = 0, len(pattern) - 1

    while left < right:
        if pattern[left] == pattern[right]:
            left += 1
            right -= 1
        else:
            return check_remove(left, right)
    
    if is_palindrome(pattern[1:]) and len(pattern[1:]) > 1:
        return pattern[1:]
    if is_palindrome(pattern[:-1]) and len(pattern[:-1]) > 1:
        return pattern[:-1]

    return None


# These are just test cases
print(find_palindrome((3, 2, 1, 1, 2, 4, 3)))  # Expected output: (3, 2, 1, 1, 2, 3)
print(find_palindrome((1, 2, 3)))             # Expected output: None
print(find_palindrome((1, 2, 1)))             # Expected output: (1, 2)
print(find_palindrome(("ab", "a", "a")))      # Expected output: None
