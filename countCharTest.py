from countChar import getCharactercount

import pytest

@pytest.mark.parametrize("char, str, expected", [
    ("a", "banana", 3),
    ("a", "bAnanA", 1),
    ("A", "banAna", 1),
    ("a", "BANANA", 0),
    ("A", "banana", 0),
    ("Z", "banana", 0),
    ("b", "b", 1),
])
def test_countCharacters(char, str, expected):
    assert getCharactercount(char, str) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])












