def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a: int
    Returns:
        True if a is two-digit number, False otherwise
    """
    return a > 9 and a < 100

print(main(15))