import pytest

from stringsInList import listUpperEle
data_getList = [
    (['Hello', 'Hello'], ['HELLO', 'HELLO']),
    (['hello', 'hello'], ['HELLO', 'HELLO']),
    (['HELLO', 'HELLO'], ['HELLO', 'HELLO']),
    ([' ', ' '],[' ', ' ']),
    ([], []),
    (['Hello', ' '], ['HELLO', ' ']),
    ([' ', 'Hello'], [' ', 'HELLO']),
    (['Hello'], ['HELLO'])
   
]
@pytest.mark.parametrize("List, expected", data_getList)
def test_ListUpperEle(List, expected):
    assert listUpperEle(List) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])
