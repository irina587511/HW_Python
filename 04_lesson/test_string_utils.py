import pytest
from string_utils import StringUtils


string_utils = StringUtils()


#  тесты для capitalize()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#  тесты для trim ()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    skypro", "skypro"),
    ("  hello world", "hello world"),
    ("Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("     123abc", "123abc"),
    ("     ", ""),
    ("", ""),
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "y"),
    ("Hello", "H"),
    ("hello", "h"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("SkyPro", ""),
    ("", "a"),
    ])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False

   #  тесты для delete_symbol()

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "y", "SkPro"),
    ("Hello", "He", "llo"),
    ("hello", "hel", "lo"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected",  [
    ("SkyPro", "b", "SkyPro"),
    ("", "a", ""),
    ("", "", "",),
])

def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
