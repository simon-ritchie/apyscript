"""Implementation of common cast conversion.

Mainly following interfaces are defined.

- to_int_from_float
    Convert float value to int.
- to_float_from_int
    Convert int value to float.
- to_bool_from_int
    Convert int value to bool.
"""


from typing import Any
from typing import Union


def to_int_from_float(
        int_or_float: Union[int, float, Any]) -> Any:
    """
    Convert float value to int.

    Parameters
    ----------
    int_or_float : int or float or NumberValueInterface
        Target float value. If integer is specified, conversion
        will be skipped.

    Returns
    -------
    int_val : int or Int
        Converted integer value.
    """
    from apyscript.type import Number
    if isinstance(int_or_float, Number):
        from apyscript.type import Int
        return Int(int_or_float)
    if not isinstance(int_or_float, float):
        return int_or_float
    return int(int_or_float)


def to_float_from_int(int_or_float: Union[int, float, Any]) -> Any:
    """
    Convert int value to float.

    Parameters
    ----------
    int_or_float : int or float or NumberValueInterface
        Target integer value. If float is specified, conversion will
        be skipped.

    Returns
    -------
    float_val : float or Number
        Converted float value.
    """
    from apyscript.type import Int
    if isinstance(int_or_float, Int):
        from apyscript.type import Number
        return Number(int_or_float)
    if not isinstance(int_or_float, int):
        return int_or_float
    return float(int_or_float)


def to_bool_from_int(integer: Union[int, Any]) -> bool:
    """
    Convert int value to bool.

    Parameters
    ----------
    integer : int or Int
        Integer value to convert.

    Returns
    -------
    bool_val : bool
        Converted boolean value.

    Raises
    ------
    ValueError
        If argument value isn't zero or one.
    """
    from apyscript.validation import number_validation
    number_validation.validate_int_is_zero_or_one(integer=integer)
    if integer == 0:
        return False
    return True
