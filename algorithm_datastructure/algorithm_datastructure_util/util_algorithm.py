import time
import unittest
import contextlib
from testfixtures import compare, Comparison as C

from .util_test import time_measure


# フィボナッチ数列
def fib(n):
    if n in (0, 1):
        return 1
    else: 
        return fib(n - 2) + fib(n - 1)


# 回文
def isPalindrome(s):
    """分割統治による回文判定

    Args:
        s (str): 回文判定する文字列
    """
    def toChars(s):
        # 全ての文字を小文字に変換
        s = s.lower()
        letters = ''
        for c in s:
            # アルファベットかどうか判定
            # [TODO] もっと効率的な条件の書き方
            #if c in 'abcdefghijklmnopqrstuvwxyz':
            # ひらがなもTrue判定になる->utf-8にエンコードすれば判定される
            # ref: https://qiita.com/fujiy/items/f738aa9d0bb7427e07a4
            if c.encode('utf-8').isalpha():
                letters = letters + c
        return letters


    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            # 再帰的に判定している
            return s[0] == s[-1] and isPal(s[1:-1])


    return isPal(toChars(s))


class TestAlgorithm(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(1, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(2, fib(2))
        self.assertEqual(13, fib(6))


    def test_isPalindrome(self):
        no_palindrome_str = "abcdef"
        palidrome_str = "abcdefedcba"
        str1 = "abcd!!!dcba"
        str2 = "abcdあいうdcba"

        self.assertFalse(isPalindrome(no_palindrome_str))
        self.assertTrue(isPalindrome(palidrome_str))
        self.assertTrue(isPalindrome(str1))
        self.assertTrue(isPalindrome(str2))


    def test_time_palindrome(self):
        """時間測定の実施
        """
        test_str1 = "abcecba"
        ret = isPalindrome(test_str1)
        self.assertTrue(ret)
        time_measure(isPalindrome)(test_str1)

        test_str2 = "abcdefgh"
        ret = isPalindrome(test_str2)
        self.assertFalse(ret)