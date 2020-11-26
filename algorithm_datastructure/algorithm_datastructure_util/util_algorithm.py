import time
import unittest
import contextlib
from testfixtures import compare, Comparison as C

from .util_test import time_measure


#
# pytestの場合
# pytest -vvv --capture=no util_algorithm.py
#


# 辞書の値を使った並べ替え
def sorted_with_dic_value(list_dic, *sort_keys):
    """辞書を要素にもつlist_dicに対して、sort_keysで指定したキーの値でソートを行い返却する。
    sort_keysには辞書のキーを指定する。
    値が同値の場合は元の順序が保持される

    Args:
        list_dic (list of dict): 辞書のリスト
        sort_key (str): 辞書のkeyを指定する。可変長引数

    Returns:
        [type]: [description]
    """
    import operator
    return sorted(list_dic, key=operator.itemgetter(*sort_keys))



# フィボナッチ関数の再帰的実装
def fastfib(n, memo={}):
    """フィボナッチ数列の計算
    メモ化。memoは再帰呼び出しによってのみ利用される

    Args:
        n ([type]): [description]
        memo (): 計算済みのフィボナッチ数列の値。memoは再帰呼び出しによってのみ利用される

    Returns:
        [type]: [description]
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastfib(n-1, memo) + fastfib(n-2, memo)
        memo[n] = result
        return result


# UnionFind
"""
UnionFindはN個のノードがいくつかのグループに分かれているときに
1. 任意の２個のノードa, bが属するグループをつなげて１つのグループにする。
2. 任意の２個のノードa, bが同じグループに属するのかを判定する
という機能に特化したデータ構造。

いずれもならし計算量log(N)で実装可能
https://www.slideshare.net/chokudai/union-find-49066733/1
https://qiita.com/Yosemat1/items/3b5f0ff6320ed63a2952
"""
class UnionFind:
    """生成時には指定した数のグループができる。グループ番号を指定して操作することができる。
    統合した場合は同じグループになる。
    tree構造で表現する。
    """
    def __init__(self, n):
        self.parents = list(range(n))

    def _root(self, x):
        """xの根を取得する

        Args:
            x ([type]): [description]

        Returns:
            int: [description]
        """
        if self.parents[x] == x:
            # 根は親が自分自身
            return x
        else:
            # 再帰して遡って根を見つける
            root = self._root(self.parents[x])
            return root

    def is_united(self, x, y):
        """2つのノードが同じグループにいるか判定する

        Args:
            x ([type]): [description]
            y ([type]): [description]

        Returns:
            boolean: 同じグループにいるならTrue。違うならFalse
        """
        # 根が同じなら同じグループ
        return self._root(x) == self._root(y)


    def union(self, x, y):
        """xが所属するグループをyが所属するグループに統合する

        Args:
            x ([type]): [description]
            y ([type]): [description]
        """
        self.parents[self._root(y)] = self._root(x) 


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


def test_sorted_with_dic_value():
    counts = [
        {'word': 'python', 'count': 3},
        {'word': 'practice', 'count': 3},
        {'word': 'book', 'count': 2}
    ]

    sorted_list = sorted_with_dic_value(counts, 'count')
    print(sorted_list)
    assert sorted_list[0]['word'] == 'book'
    assert sorted_list[1]['word'] == 'python'

    sorted_list = sorted_with_dic_value(counts, 'count', 'word')
    assert sorted_list[1]['word'] == 'practice'



def test_fastfib():
    result = fastfib(6)
    assert result == 13
    time_measure(fastfib)(6)
    result = fastfib(120)

    time_measure(fastfib)(120)



class TestAlgorithm(unittest.TestCase):

    def test_unionfind(self, parameter_list=[5]):
        for group_num in parameter_list:
            uf = UnionFind(group_num)
            uf.union(0, 3)
            uf.union(1, 3)
            self.assertTrue(uf.is_united(0, 1))



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