import pytest

from upperCase import convertToUpper


@pytest.mark.parametrize("word, expected", [
    ("Hello", "HELLO"),
    ("hello", "HELLO"),
    ("HELLO", "HELLO"),
    (" ", " "),
    ("", ""),
    ("Hello World", "HELLO WORLD")
])
def test_convertToUpper(word,  expected):
    assert convertToUpper(word) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])
