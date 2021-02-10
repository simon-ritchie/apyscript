"""Implementations to manipulate each scopes variable name
related interface.
"""

import os
from typing import List

from apyscript.expression import expression_file_util, expression_scope
from apyscript.file import file_util


def get_current_scope_next_variable_name(type_name: str) -> str:
    """
    Get current scope's next variable name of specified type name.

    Notes
    -----
    If call this function multiple times, then returned number will be
    increased.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
        If `sprite` is specified and there is no `sprite` variable
        name in expression file, then `sprite_1` will be returned.
        If variable name of `sprite_1` is already used, then `sprite_2`
        will be returned.

    Returns
    -------
    variable_name : str
        Current scope's next variable name.
    """
    next_variable_num: int = _get_current_scope_next_variable_num(
        type_name=type_name)
    variable_name = _make_variable_name(
        type_name=type_name, variable_num=next_variable_num)
    _save_next_variable_name_to_current_scope_file(type_name=type_name)
    return variable_name


def _make_variable_name(type_name: str, variable_num: int) -> str:
    """
    Make variable name from type name and variable num.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
    variable_num : int
        Target variable number (start from 1).

    Returns
    -------
    variable_name : str
        Variable name that concatenated type name and variable number.
    """
    variable_name: str = f'{type_name}_{variable_num}'
    return variable_name


def _get_current_scope_next_variable_num(type_name: str) -> int:
    """
    Get current scope's next variable number.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    next_variable_num : int
        Next variable number (start from 1).
    """
    variable_names: List[str] = _read_current_scope_variable_names(
        type_name= type_name)
    if not variable_names:
        return 1
    last_num: int = int(variable_names[-1].split('_')[-1])
    return last_num + 1


def _read_current_scope_variable_names(type_name: str) -> List[str]:
    """
    Read current scope's variable names from file.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    variable_names : list of str
        Target type name's variable names.
        e.g., if type name is sprite, `['sprite_1', 'sprite_2', ...]`.
    """
    file_path: str = get_current_scope_variable_names_file_path(
        type_name=type_name)
    if not os.path.isfile(file_path):
        return []
    variables_str: str = file_util.read_txt(file_path=file_path)
    variables_str = variables_str.strip(',')
    variable_names: List[str] = variables_str.split(',')
    return variable_names


def _save_next_variable_name_to_current_scope_file(type_name: str) -> None:
    """
    Save current scope's next variable name to file.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.
    """
    file_path: str = get_current_scope_variable_names_file_path(
        type_name=type_name)
    next_variable_num: int = _get_current_scope_next_variable_num(
        type_name=type_name)
    variable_name: str = _make_variable_name(
        type_name=type_name, variable_num=next_variable_num)
    file_util.append_plain_txt(
        txt=f'{variable_name},', file_path=file_path)


def get_current_scope_variable_names_file_path(type_name: str) -> str:
    """
    Get current scope's file path of saving variable names.

    Parameters
    ----------
    type_name : str
        Any type name, e.g., `sprite`.

    Returns
    -------
    file_path : str
        Specified type name's target file path.
    """
    current_scope: str = expression_scope.get_current_scope()
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'scope_variables_{current_scope}_{type_name}.txt',
    )
    return file_path