import time, sys, os
import unittest
import contextlib
import pytest
from testfixtures import compare, Comparison as C
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithm_datastructure import time_measure

"""
 pytest -vvv --capture=no input.py
 * --capture=no テストをpassしてもprintを表示させる
"""

# 標準入出力が使われた処理のテスト
# ref: https://qiita.com/podhmo/items/70a78c1429525dde0a48
class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"

class StdinBuffer():
    def __init__(self):
        from io import StringIO
        self.buf = StringIO()

    def write_stdin(self, data):
        self.buf.write("{}\n".format(data))
        self.buf.seek(0)

        return self.buf


def example_simple_input():
    """ [1, 2, 3]を数値に変換して変数に書く
    """
    from io import StringIO
    buf = StringIO()
    buf.write("1 2 3\n")
    buf.seek(0)

    print("[1, 2, 3]を数値に変換して変数に書く")
    with redirect_stdin(buf):
        x, y, z = map(int, input().split())

    print("{} {} {} type(x):{}".format(x, y, z, type(x)))


def test_input():
    example_simple_input()