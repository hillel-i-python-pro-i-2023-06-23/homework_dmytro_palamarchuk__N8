"""Utility"""


def peek(iterator):
    """
    Returns the first element from the iterator without moving the pointer.

    Args:
        iterator: An iterator or iterable object.

    Returns:
        object: The first element of the iterator, or None if the iterator is empty.
    """
    try:
        first_value = next(iterator)
    except StopIteration:
        return None

    return first_value


def pounds_to_kg(pounds: float) -> float:
    """Converts pounds to kg"""
    return pounds * 0.45359237


def inches_to_cm(length: float) -> float:
    """Converts inches to cm"""
    return length * 2.54
