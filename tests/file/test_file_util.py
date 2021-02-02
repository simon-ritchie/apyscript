import os
import shutil

from apyscript.file import file_util
from tests import testing_helper


def test_empty_directory() -> None:
    tmp_dir_path: str = '../.tmp_apyscript/'
    os.makedirs(tmp_dir_path, exist_ok=True)
    test_file_path: str = os.path.join(tmp_dir_path, 'test.txt')
    testing_helper.make_blank_file(file_path=test_file_path)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)
    assert len(os.listdir(tmp_dir_path)) == 0

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)