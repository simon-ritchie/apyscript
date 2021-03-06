from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type import Boolean
from apyscript.type import Int
from apyscript.type import String
from tests import testing_helper


class TestString:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__get_str_value(self) -> None:
        string_1: String = String('Hello!')
        value: str = string_1._get_str_value(value='World!')
        assert value == 'World!'
        value = string_1._get_str_value(value=string_1)
        assert value == 'Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=String,
            kwargs={'value': 100})

        string_1: String = String(value='Hello!')
        expected_attrs: Dict[str, Any] = {
            '_initial_value': 'Hello!',
            '_value': 'Hello!',
            '_type_name': 'string',
        }
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=string_1)
        assert string_1.variable_name.startswith('string_')

        string_2: String = String(value=string_1)
        assert string_2._value == 'Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_constructor_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {string_1.variable_name} = "Hello!";'
        )
        assert expected in expression

        string_2: String = String(value=string_1)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {string_2.variable_name} = {string_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_value(self) -> None:
        string_1: String = String(value='Hello!')
        string_1.value = 'World!'
        assert string_1.value == 'World!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_value_setter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        string_1.value = 'World!'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{string_1.variable_name} = "World!";'
        )
        assert expected in expression

        string_2: String = String(value='')
        string_2.value = string_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{string_2.variable_name} = {string_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___add__(self) -> None:
        string_1: String = String(value='Hello')
        string_2: String = string_1 + ' World!'
        assert string_2._value == 'Hello World!'

        string_3: String = String(value=' apyscript!')
        string_4: String = string_1 + string_3
        assert string_4._value == 'Hello apyscript!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_addition_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        string_2: String = string_1 + ' World!'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {string_2.variable_name} = {string_1.variable_name}'
            ' + " World!";'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___mul__(self) -> None:
        string_1: String = String(value='Hello!')
        string_2: String = string_1 * 3
        assert string_2.value == 'Hello!Hello!Hello!'

        string_3: String = string_1 * Int(2)
        assert string_3.value == 'Hello!Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_multiplication_expression(self) -> None:
        expression_file_util.remove_expression_file()
        string_1: String = String(value='Hello!')
        string_2: String = string_1 * 3
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {string_2.variable_name} = "";'
            '\nfor (var i = 0; i < 3; i++) {'
            f'\n  {string_2.variable_name} += {string_1.variable_name};'
            '\n}'
        )
        assert expected in expression

        int_1: Int = Int(2)
        _: String = string_1 * int_1
        expression = expression_file_util.get_current_expression()
        expected = (
            f'\nfor (var i = 0; i < {int_1.variable_name}; i++) {{'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___iadd__(self) -> None:
        string_1: String = String(value='Hello')
        string_1 += ' World!'
        assert string_1.value == 'Hello World!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___imul__(self) -> None:
        string_1: String = String(value='Hello!')
        string_1 *= 3
        assert string_1.value == 'Hello!Hello!Hello!'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___str__(self) -> None:
        string_1: String = String(value='Hello!')
        result: str = str(string_1)
        assert result == 'Hello!'
        assert isinstance(result, str)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___eq__(self) -> None:
        string_1: String = String(value='Hello!')
        assert string_1 == 'Hello!'
        string_2: String = String(value='Hello!')
        assert string_1 == string_2
        assert not string_1 == 'World!'
        assert not string_1 == 100

        assert isinstance(string_1 == 'Hello!', Boolean)
        assert isinstance(string_1 == string_2, Boolean)
        assert isinstance(string_1 == 100, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___ne__(self) -> None:
        string_1: String = String(value='Hello!')
        assert string_1 != 'World'
        assert string_1 != String('World!')
        assert string_1 != 100

        assert isinstance(string_1 != 'World', Boolean)
        assert isinstance(string_1 != String('World'), Boolean)
        assert isinstance(string_1 != 100, Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___lt__(self) -> None:
        string_1: String = String(value='1970-01-02')
        assert string_1 < '1970-01-03'
        string_2: String = String(value='1970-01-03')
        assert string_1 < string_2
        assert not string_1 < '1970-01-02'

        assert isinstance(string_1 < '1970-01-03', Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___le__(self) -> None:
        string_1: String = String(value='1970-01-02')
        assert string_1 <= '1970-01-02'
        assert string_1 <= '1970-01-03'
        string_2: String = String(value='1970-01-02')
        assert string_1 <= string_2
        assert not string_1 <= '1970-01-01'

        assert isinstance(string_1 <= '1970-01-02', Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___gt__(self) -> None:
        string_1: String = String(value='1970-01-02')
        assert string_1 > '1970-01-01'
        string_2: String = String(value='1970-01-01')
        assert string_1 > string_2
        assert not string_1 > '1970-01-02'

        assert isinstance(string_1 > '1970-01-01', Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___ge__(self) -> None:
        string_1: String = String(value='1970-01-02')
        assert string_1 >= '1970-01-02'
        assert string_1 >= '1970-01-01'
        string_2: String = String(value='1970-01-02')
        assert string_1 >= string_2
        assert not string_1 >= '1970-01-03'

        assert isinstance(string_1 >= '1970-01-02', Boolean)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___int__(self) -> None:
        string_1: String = String(value='100')
        assert int(string_1) == 100

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___float__(self) -> None:
        string_1: String = String(value='100.5')
        assert float(string_1) == 100.5

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___repr__(self) -> None:
        string_1: String = String(value='Hello!')
        assert repr(string_1) == "String('Hello!')"
