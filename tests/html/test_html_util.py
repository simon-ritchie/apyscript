from typing import Dict
from typing import List
from typing import Tuple

from apyscript.html import html_util
from apyscript.html.html_util import ScriptLineUtil
from tests import testing_helper


def test_remove_first_selector_symbol_char() -> None:
    str_val: str = html_util.remove_first_selector_symbol_char(
        str_val='.line-graph')
    assert str_val == 'line-graph'

    str_val = html_util.remove_first_selector_symbol_char(
        str_val='#line-graph')
    assert str_val == 'line-graph'

    str_val = html_util.remove_first_selector_symbol_char(
        str_val='line-graph')
    assert str_val == 'line-graph'


def test_append_html_to_str() -> None:
    result: str = html_util.append_html_to_str(
        to_append_html='<body>',
        dest_html='<html>',
        indent_num=1)
    expected_str: str = (
        '<html>'
        '\n  <body>'
    )
    assert result == expected_str

    result = html_util.append_html_to_str(
        to_append_html='<html>',
        dest_html='',
        indent_num=0)
    assert result == '<html>'


def test_append_indent_to_each_script_line() -> None:
    html: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\nconsole.log("Hello!");'
        '\nconsole.log("World!");'
        '\n</script>'
        '\n</html>'
    )
    result_html: str = html_util.append_indent_to_each_script_line(
        html=html, indent_num=1)
    expected_html: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\n  console.log("Hello!");'
        '\n  console.log("World!");'
        '\n</script>'
        '\n</html>'
    )
    assert result_html == expected_html


def test_is_script_start_tag_line() -> None:
    result: bool = html_util.is_script_start_tag_line(
        line='<html>')
    assert not result

    result = html_util.is_script_start_tag_line(
        line='<script type="text/javascript" src="./jquery.js"></script>')
    assert not result

    result = html_util.is_script_start_tag_line(
        line='<script type="text/javascript">')
    assert result


def test_is_script_end_tag_line() -> None:
    result: bool = html_util.is_script_end_tag_line(line='<html>')
    assert not result

    result = html_util.is_script_end_tag_line(
        line='<script src="jquery.min.js"></script>')
    assert not result

    result = html_util.is_script_end_tag_line(line='</script>')
    assert result


class TestScriptLineUtil:

    _TEST_HTML: str = (
        '<html>'
        '\n<script type="text/javascript">'
        '\nconsole.log('
        '\n  "Hello apyscript!");'
        '\n</script>'
        '\n<span>It is not in the stars to hold our destiny.</span>'
        '\n<script type="text/javascript">'
        '\nconsole.log("Hello apyscript!");'
        '\n</script>'
        '\n</html>'
    )

    def test___init__(self) -> None:
        html: str = '<html>\n</html>'
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=html)
        testing_helper.assert_attrs(
            expected_attrs={
                'html': html,
                'script_line_ranges': [],
            },
            any_obj=script_line_util,
        )

    def test__set_script_line_ranges(self) -> None:
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=self._TEST_HTML)
        expected: List[Tuple[int, int]] = [
            (3, 4),
            (8, 8),
        ]
        assert script_line_util.script_line_ranges == expected

    def test_is_script_line(self) -> None:
        script_line_util: ScriptLineUtil = ScriptLineUtil(
            html=self._TEST_HTML)

        expected_values: Dict[int, bool] = {
            2: False,
            3: True,
            4: True,
            5: False,
            7: False,
            8: True,
            9: False,
        }
        for line_number, expected in expected_values.items():
            result: bool = script_line_util.is_script_line(
                line_number=line_number)
            assert result == expected


def test_wrap_expression_by_script_tag() -> None:
    expression: str = 'console.log("Hello!");'
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    assert expression == (
        '<script type="text/javascript">'
        '\nconsole.log("Hello!");'
        '\n</script>'
    )
