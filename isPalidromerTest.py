import pytest

from isPalindrome import checkPalindrome


@pytest.mark.parametrize("word, expected", [
    ("Apple", False),
    ("racecar", True),
    (" ", True),
    ("Hello World", False),
    ("Hello olleH", True),
     ("H", True)


])
def test_checkPalindrome(word,  expected):
    assert checkPalindrome(word) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])