"""Implementations of Rectangle class and other interfaces.
"""

from typing import Any

from apyscript.display.graphic_base import GraphicBase
from apyscript.display.height_interface import HeightInterface
from apyscript.display.stage import get_stage_variable_name
from apyscript.display.width_interface import WidthInterface
from apyscript.expression import expression_file_util
from apyscript.expression import scope_variables_util
from apyscript.html import html_const
from apyscript.validation import size_validation


class Rectangle(GraphicBase, WidthInterface, HeightInterface):

    def __init__(
            self, parent: Any, x: int, y: int, width: int,
            height: int) -> None:
        """
        Create a rectangle vector graphic.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        x : int
            X position to start drawing.
        y : int
            Y position to start drawing.
        width : int
            Rectangle width.
        height : int
            Rectangle height.
        """
        variable_name: str = scope_variables_util.\
            get_current_scope_next_variable_name(type_name='rectangle')
        super(Rectangle, self).__init__(
            parent=parent, x=x, y=y, variable_name=variable_name)
        size_validation.validate_size_is_gte_zero(size=width)
        size_validation.validate_size_is_gte_zero(size=height)
        self.width = width
        self.height = height


def append_draw_rect_expression(rectangle: Rectangle) -> None:
    """
    Append Graphics's draw_rect interface expression to the file
    of current scope.

    Parameters
    ----------
    rectangle : Rectanble
        Created rectangle instance.
    """
    from apyscript.display.sprite import Sprite
    sprite: Sprite = rectangle.parent.parent
    variable_name: str = rectangle.variable_name
    stage_variable_name: str = get_stage_variable_name()
    expression: str = (
        f'{html_const.SCRIPT_START_TAG}'
        f'\nvar {variable_name} = {stage_variable_name}'
        f'\n  .rect({rectangle.width}, {rectangle.height})'
    )
    attrs_str: str = _make_rect_attrs_expression(rectangle=rectangle)
    expression += f'{attrs_str};'
    add_child_exp: str = sprite.make_add_child_expression(
        child_variable_name=rectangle.variable_name)
    expression += f'\n{add_child_exp}'
    expression += f'\n{html_const.SCRIPT_END_TAG}'
    expression_file_util.append_expression_to_current_scope(
        expression=expression)


def _make_rect_attrs_expression(rectangle: Rectangle) -> str:
    """
    Make rectangle attributes expression string.

    Parameters
    ----------
    rectangle : Rectangle
        Target rectangle instance.

    Returns
    -------
    rect_attrs_expression : str
        Rectangle attributes expression string.
    """
    from apyscript.display.graphics import Graphics
    from apyscript.display import graphics_expression
    graphics: Graphics = rectangle.parent
    INDENT_NUM: int = 2
    rect_attrs_expression: str = '\n  .attr({'
    rect_attrs_expression = graphics_expression.append_fill_expression(
        graphics=graphics, expression=rect_attrs_expression,
        indent_num=INDENT_NUM)
    rect_attrs_expression = \
        graphics_expression.append_fill_opacity_expression(
            graphics=graphics, expression=rect_attrs_expression,
            indent_num=INDENT_NUM)
    rect_attrs_expression = graphics_expression.append_x_expression(
        graphic=rectangle, expression=rect_attrs_expression,
        indent_num=INDENT_NUM)
    rect_attrs_expression = graphics_expression.append_y_expression(
        graphic=rectangle, expression=rect_attrs_expression,
        indent_num=INDENT_NUM)
    rect_attrs_expression += '\n  })'
    return rect_attrs_expression
