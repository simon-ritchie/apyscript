from random import randint
from typing import List

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.file import file_util


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test_get_variable_names_file_path() -> None:
    file_path: str = expression_variables_util.\
        get_variable_names_file_path(type_name='sprite')
    assert file_path.startswith(expression_file_util.EXPRESSION_ROOT_DIR)
    assert file_path.endswith('variables_sprite.txt')


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__read_variable_names() -> None:
    file_path: str = expression_variables_util.\
        get_variable_names_file_path(type_name='sprite')
    file_util.save_plain_txt(
        txt='sprite_1,sprite_2,sprite_3,', file_path=file_path)
    variable_names: List[str] = expression_variables_util.\
        _read_variable_names(type_name='sprite')
    assert variable_names == ['sprite_1', 'sprite_2', 'sprite_3']

    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__get_next_variable_num() -> None:
    file_path: str = expression_variables_util.\
        get_variable_names_file_path(type_name='sprite')
    file_util.remove_file_if_exists(file_path=file_path)
    next_variable_num: int = expression_variables_util.\
        _get_next_variable_num(type_name='sprite')
    assert next_variable_num == 1

    file_util.save_plain_txt(
        txt='sprite_1,sprite_2,', file_path=file_path)
    next_variable_num = expression_variables_util.\
        _get_next_variable_num(type_name='sprite')
    assert next_variable_num == 3

    file_util.remove_file_if_exists(file_path=file_path)


def test__make_variable_name() -> None:
    variable_name: str = expression_variables_util._make_variable_name(
        type_name='sprite', variable_num=3)
    assert variable_name == 'sprite_3'


@retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
def test__save_next_variable_name_to_file() -> None:
    file_path: str = expression_variables_util.\
        get_variable_names_file_path(type_name='sprite')
    file_util.remove_file_if_exists(file_path=file_path)
    expression_variables_util._save_next_variable_name_to_file(
        type_name='sprite')
    next_variable_num: int = expression_variables_util.\
        _get_next_variable_num(type_name='sprite')
    assert next_variable_num == 2
    expression_variables_util._save_next_variable_name_to_file(
        type_name='sprite')
    next_variable_num = expression_variables_util.\
        _get_next_variable_num(type_name='sprite')
    assert next_variable_num == 3

    file_util.remove_file_if_exists(file_path=file_path)


def test_get_next_variable_name() -> None:
    file_path: str = expression_variables_util.\
        get_variable_names_file_path(type_name='sprite')
    file_util.remove_file_if_exists(file_path=file_path)

    variable_name: str = expression_variables_util.\
        get_next_variable_name(type_name='sprite')
    assert variable_name == 'sprite_1'

    variable_name = expression_variables_util.\
        get_next_variable_name(type_name='sprite')
    assert variable_name == 'sprite_2'

    file_util.remove_file_if_exists(file_path=file_path)
