"""Class implementation for line alpha interface.
"""

from typing import Optional

from apyscript.display.variable_name_interface import VariableNameInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.validation import color_validation
from apyscript.validation import number_validation


class LineAlphaInterface(VariableNameInterface):

    _line_alpha: Optional[float] = None

    @property
    def line_alpha(self) -> Optional[float]:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : float or None
            Current line alpha (opacity. 0.0 to 1.0).
            If not be set, None will be returned.
        """
        return self._line_alpha

    @line_alpha.setter
    def line_alpha(self, value: float) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : float
            Line alpha (opacity) to set.
        """
        self.update_line_alpha_and_skip_appending_exp(value=value)
        self._append_line_alpha_update_expression()

    def _append_line_alpha_update_expression(self) -> None:
        """
        Append line alpha updating expression to current scope.
        """
        expression: str = (
            f'{self.variable_name}.stroke({{opacity: {self.line_alpha}}});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression_to_current_scope(
            expression=expression)

    def update_line_alpha_and_skip_appending_exp(self, value: float) -> None:
        """
        Update line alpha and skip appending expression to file.

        Parameters
        ----------
        value : float
            Line alpha (opacity) to set.
        """
        number_validation.validate_num(num=value)
        color_validation.validate_alpha_range(alpha=value)
        self._line_alpha = value