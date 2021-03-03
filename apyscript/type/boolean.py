"""Class implementation for boolean.
"""

from typing import Any, Union
from apyscript.type.copy_interface import CopyInterface
from apyscript.validation import number_validation
from apyscript.converter import cast
from apyscript.validation import bool_validation
from apyscript.expression import expression_variables_util
from apyscript.expression import expression_file_util
from apyscript.type.variable_name_interface import VariableNameInterface


class Boolean(CopyInterface):

    _initial_value: Union[bool, int, Any]
    _value: bool

    def __init__(self, value: Union[bool, int, Any]) -> None:
        """
        Boolean class for apyscript library.

        Parameters
        ----------
        value : bool or int or Boolean or Int
            Initial boolean value. 0 or 1 are acceptable for integer
            value.
        """
        from apyscript.type.number_value_interface import NumberValueInterface
        TYPE_NAME: str = 'boolean'
        number_validation.validate_int_is_zero_or_one(integer=value)
        self._initial_value = value
        if isinstance(value, (int, float, NumberValueInterface)):
            value_: bool = cast.to_bool_from_int(integer=value)
        elif isinstance(value, Boolean):
            value_ = value._value
        else:
            value_ = value
        bool_validation.validate_bool(value=value_)
        self._value = value_
        self._type_name = TYPE_NAME
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=TYPE_NAME)
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        expression: str = f'var {self.variable_name} = '
        if isinstance(self._initial_value, VariableNameInterface):
            expression += f'Boolean({self._initial_value.variable_name});'
        elif self._value:
            expression += 'true;'
        else:
            expression += 'false;'
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
