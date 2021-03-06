"""Test project for `trace` interface.

Command examples:
$ python test_projects/trace/main.py
$ python trace/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.trace import trace
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter

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
        stage_width=100, stage_height=100)
    trace(stage, 100, "Hello!")

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
