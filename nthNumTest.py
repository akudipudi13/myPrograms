import pytest


from printNthNum import nthNum


@pytest.mark.parametrize("list, expected", [
    ("1 2 3 4", "1\n4\n2\n3"),
    ("1 2 3 4 5", "1\n5\n2\n4\n3"),
    ("1 2", "1\n2"),
    (" ", ""),
    ("1 66 78", "1\n78\n66"),
    ("2", "2")
])
def test_checkDuplicates(capsys, list, expected):
    nthNum(list.split())   
    captured = capsys.readouterr()
    assert expected in captured.out


if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])