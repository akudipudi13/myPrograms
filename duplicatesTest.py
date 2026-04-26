import pytest


from duplicates import Findduplicates


@pytest.mark.parametrize("list, expected", [
    ("3 5 3 6", "3"),
    ("5 6 7 8", ""),
    ("5 6 7 7", "7"),
    ("6 6 8 8", "6\n8"),
    ("3 5 6 3", "3"),
    ("7 9   9 3", "9")
])
def test_checkDuplicates(capsys, list, expected):
    Findduplicates(list.split())   
    captured = capsys.readouterr()
    assert expected in captured.out


if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])