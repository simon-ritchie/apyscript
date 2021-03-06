from random import randint

from retrying import retry

from apyscript.display.width_interface import WidthInterface
from apyscript.expression import expression_file_util
from apyscript.type import Int


class TestWidthInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_width(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        width_interface.width = Int(100)
        assert width_interface.width == 100

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_width_update_expression(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        expression_file_util.remove_expression_file()
        width_interface.width = Int(200)
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_width_interface.width(200);'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_update_width_and_skip_appending_exp(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        expression_file_util.remove_expression_file()
        width_interface.update_width_and_skip_appending_exp(
            value=Int(300))
        assert width_interface.width == 300
        expression: str = expression_file_util.get_current_expression()
        assert 'width(' not in expression
