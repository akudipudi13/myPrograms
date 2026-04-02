
'''
def test_line_wrapping_function():
    assert lineWrapping('hello') == 'hello'
    assert lineWrapping('hi hi') == 'hi hi'
    assert lineWrapping('Special') == 'Special'
    assert lineWrapping('Hello Hello') == 'Hello\nHello'
    assert lineWrapping('') == 'Empty string! Error!'
    assert lineWrapping('      ') == '     \n '
    assert lineWrapping('I am Akhil, and I like programming') == 'I am\nAkhil\nandI\nlike\nprogramming'

'''
#How to unit test a function that onrints in screen. whether the printed message is on expected lines.
#Mocking print in pytest.

import sys

from log_wrapping import lineWrapping

def test_lineWrapping(capsys):
    # 1. Basic stdout check
    lineWrapping("hello")
    captured = capsys.readouterr()
    assert "hello" in captured.out
    

    lineWrapping("hi hi")
    captured = capsys.readouterr()
    assert "hi hi" in captured.out
    

    lineWrapping("Special")
    captured = capsys.readouterr()
    assert "Special" in captured.out
    
    lineWrapping("Hello Hello")
    captured = capsys.readouterr()
    assert "Hello\nHello" in captured.out

    lineWrapping("")
    captured = capsys.readouterr()
    assert "Empty string! Error!" in captured.out

    lineWrapping("       ")
    captured = capsys.readouterr()
    assert "     \n " in captured.out

    lineWrapping("I am a student and I like to code in class")
    captured = capsys.readouterr()
    assert "I am\na\nstudent\nand I\nlike\nto\ncode\nin\nclass" in captured.out

    