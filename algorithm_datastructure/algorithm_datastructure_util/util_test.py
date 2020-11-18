import time
import unittest
import contextlib
from testfixtures import compare, Comparison as C


"""
 pytest -vvv --capture=no util_test.py
 * --capture=no テストをpassしてもprintを表示させる
"""


def print_list_2d(l_2d):
    """2次元リストの要素数を表示する

    Args:
        l_2d ([type]): [description]
    """
    return [len(v) for v in l_2d]


def time_measure(func):
    """メソッド処理時間を測定する
    """
    def wrapper(*args, **kargs):
        start_time = time.perf_counter()
        
        result = func(*args, **kargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        # https://www.headboost.jp/python-print-handle-number-of-digits/
        # fプリフィックスにおける桁数指定
        print(f'{func.__name__}: {execution_time:.6f} [s]')
        return result
    return wrapper


# 標準入出力が使われた処理のテスト
# ref: https://qiita.com/podhmo/items/70a78c1429525dde0a48
class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"


class TestSample(unittest.TestCase):

    def test_stdin(self):
        """標準入出力が使われた処理のテスト
        """
        from io import StringIO
        buf = StringIO()
        buf.write("hello\n")
        buf.seek(0)

        with redirect_stdin(buf):
            actual = input()

        expected = "hello"
        self.assertEqual(actual, expected)


    def test_mock(self):
        """mockの利用
        """
        from unittest import mock

        m = mock.Mock()
        m.something("this is dummy-arg")

        # 戻り値を指定
        m.something.return_value = 10
        print(m.something("this is dummy-arg"))

        # モックメソッドの呼び出しの確認
        print("m.something.called: {}".format(m.something.called))
        print("m.somethink.call_args: {}".format(m.something.call_args))

        # Exceptionの送出指定
        from testfixtures import ShouldRaise
        with ShouldRaise(Exception('oops')):
            m.something.side_effect = Exception('oops')
            m.something("this is dummy-arg")


    def test_knapsack_greedy(self):
        """greedyアルゴリズムのテスト
        """
        pass
