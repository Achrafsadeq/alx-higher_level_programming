#!/usr/bin/python3
def safe_print_integer(value):
    """Attempt to print an integer using formatted string.

    Args:
        value: Any input, expected to be an integer.

    Returns:
        True if successfully printed, False otherwise.
    """
    result = False
    try:
        print(f"{int(value)}")
        result = True
    except (TypeError, ValueError):
        pass
    return result
