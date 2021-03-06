"""Test project for draw_rect interface.

Command examples:
$ python test_projects/draw_rect/main.py
$ python draw_rect/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.assertion import assert_not_equal
from apyscript.display import Sprite
from apyscript.display.rectangle import Rectangle
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import Int
from apyscript.type import Number

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)

    # Basic functional test case.
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')
    sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    stage.add_child(child=sprite)

    # Test for begin_fill interface.
    sprite.graphics.begin_fill(color='#00aaff', alpha=0.5)
    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

    # Test for line_style interface.
    sprite.graphics.begin_fill(color='#00aaff')
    sprite.graphics.line_style(color='#fff', thickness=3, alpha=0.7)
    sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)

    # Test for rectangle x position update.
    rectangle: Rectangle = sprite.graphics.draw_rect(
        x=0, y=50, width=50, height=50)
    rectangle.x = Int(350)

    # Test for rectangle y position update.
    rectangle = sprite.graphics.draw_rect(
        x=450, y=0, width=50, height=50)
    rectangle.y = Int(50)

    # Test for rectangle width update.
    rectangle = sprite.graphics.draw_rect(
        x=550, y=50, width=50, height=50)
    rectangle.width = Int(100)

    # Test for rectangle height update.
    rectangle = sprite.graphics.draw_rect(
        x=700, y=50, width=50, height=50)
    rectangle.height = Int(100)

    # Test for rectangle fill color update.
    rectangle = sprite.graphics.draw_rect(
        x=800, y=50, width=50, height=50)
    rectangle.fill_color = '#f0a'

    # Test for rectangle fill alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=900, y=50, width=50, height=50)
    rectangle.fill_alpha = Number(0.5)

    # Test for rectangle line color update.
    rectangle = sprite.graphics.draw_rect(
        x=50, y=150, width=50, height=50)
    rectangle.line_color = '#f0a'

    # Test for rectangle line thickness update.
    rectangle = sprite.graphics.draw_rect(
        x=150, y=150, width=50, height=50)
    rectangle.line_thickness = Int(1)

    # Test for rectangle line alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=250, y=150, width=50, height=50)
    rectangle.line_alpha = Number(1.0)

    _another_func(stage=stage, sprite=sprite)

    sprite.graphics.draw_rect(
        x=450, y=150, width=50, height=50)

    # Test for rectangle fill alpha update with Number.
    number_1: Number = Number(0.725)
    rectangle = sprite.graphics.draw_rect(
        x=550, y=150, width=50, height=50)
    rectangle.fill_alpha = number_1

    # Test for each attribute values are immutable.
    rectangle.fill_alpha = Number(0.5)
    fill_alpha: Number = rectangle.fill_alpha
    fill_alpha += 0.2
    assert_not_equal(expected=fill_alpha, actual=rectangle.fill_alpha)

    rectangle.x = Int(550)
    x: Int = rectangle.x
    x += 100
    assert_not_equal(expected=x, actual=rectangle.x)

    rectangle.y = Int(150)
    y: Int = rectangle.y
    y += 100
    assert_not_equal(expected=y, actual=rectangle.y)

    rectangle.line_thickness = Int(2)
    line_thickness: Int = rectangle.line_thickness
    line_thickness += 1
    assert_not_equal(
        expected=line_thickness, actual=rectangle.line_thickness)

    rectangle.line_alpha = Number(0.5)
    line_alpha: Number = rectangle.line_alpha
    line_alpha += 0.2
    assert_not_equal(expected=line_alpha, actual=rectangle.line_alpha)

    width: Int = rectangle.width
    width = Int(150)
    assert_not_equal(expected=width, actual=rectangle.width)

    height: Int = rectangle.height
    height = Int(200)
    assert_not_equal(expected=height, actual=rectangle.height)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def _another_func(stage: Stage, sprite: Sprite) -> None:
    """
    Another function to test expression and arguments behavior.

    Parameters
    ----------
    stage : Stage
        Stage instance.
    sprite : Sprite
        Sprite instance.
    """
    sprite.graphics.begin_fill(color='#f0a')
    sprite.graphics.draw_rect(x=350, y=150, width=50, height=50)
    stage.add_child(child=sprite)


if __name__ == '__main__':
    main()
