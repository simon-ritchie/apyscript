from apyscript.validation import color_validation
from tests import testing_helper


def test_validate_hex_color_code_format() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': 10})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': '33'}
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_hex_color_code_format,
        kwargs={'hex_color_code': 'gggggg'})


def test_validate_alpha_range() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_alpha_range,
        kwargs={'alpha': -0.1})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=color_validation.validate_alpha_range,
        kwargs={'alpha': 1.1})

    color_validation.validate_alpha_range(alpha=0.0)
    color_validation.validate_alpha_range(alpha=1.0)
