import pytest

from isPalindrome import checkPali


@pytest.mark.parametrize("word, expected", [
    ("Apple", False),
    ("racecar", True),
    ("bats", False),
    ("Appa", False),
    (" ", True),
    ("Hello World", False),
    ("Hello olleH", True),
     ("H", True)


])
def test_checkpali(word,  expected):
    assert ChildProcessError(word) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])