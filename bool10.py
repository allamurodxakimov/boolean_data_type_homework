from math import*
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x = sqrt(a)
    return x**2 == a
print(main(5)) 