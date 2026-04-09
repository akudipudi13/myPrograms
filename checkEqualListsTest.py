import pytest

from checkEqualLists import checkEqualList



@pytest.mark.parametrize("list1, list2, expected", [
    ("1 2 3 4 5", "1 2 3 4 5", "equal"),
    ("1 1 1 1 1", "1 2 3 4 5", "not equal"),
    ("1", "1 2", "not equal"),
    ("1", "1 1", "not equal"),
    ("1 2 3", " ", "not equal"),
    (" ", "1 2 3", "not equal"),
    ("1 2 3 4", "1 2 3 5", "not equal"),
    ("5 4 3 2 1 ", "6 4 3 2 1", "not equal")
])
def test_countCharacters(list1, list2, expected):
    assert checkEqualList(list1, list2) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])
