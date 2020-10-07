import time, sys, os
import unittest
import contextlib
import pytest
from testfixtures import compare, Comparison as C

from .item import Item
from .item import value
from .item import weight_inverse
from .item import density

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithm_datastructure_util import time_measure
# errorになる
# from algorithm_datastructure_util import time_measure


def choose_best(pset, max_weight, get_val, get_weight):
    """max_weight内で最も価値が高くなるitemの組み合わせを力づくで抽出する。
    全ての組み合わせを列挙し、重量制限を超える組み合わせを取り除き、
    残された組み合わせで総価値が最も大きいものを選ぶ

    Args:
        pset ([type]): [description]
        max_weight ([type]): [description]
        get_val ([type]): [description]
        get_weight ([type]): [description]
    """
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items

    return (best_set, best_val)




def greedy(items, max_weight, key_function):
    """与えられたitemの中で最も価値の高い品物を選ぶことを繰り返す。
    価値を定義するのがkey_functionである。itemsはリスト、max_weight>=0とする
    """
    # key: リストの各要素を呼び出す前に適用するメソッド
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if(total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)


# [TODO] items.pyへの移行
def get_item_names_from_list(items_list):
    """
    itemのリストから名前リストだけ取り出す
    """
    names = []
    for item in items_list:
        names.append(item.get_name())
    return names


# [TODO] items.pyへの移行
def display_items_list(items, val):
    print('Total valud of items taken is ', val)
    for item in items:
        print(' ', item) 



def get_binary_rep(n, num_digits):
    """nとnum_digitsを非負のint型とする。
    nの値を, num_digits桁の2進数で表す文字列を返却する

    Args:
        n ([type]): [description]
        num_digits ([type]): [description]
    """
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result 
    return result



def get_powerset(items):
    """リストitemsの全ての可能な組み合わせからなるリストを返却する
    [1, 2] ならば [], [1], [2], [1, 2] を要素にもつリストを返却する

    Args:
        items ([type]): [description]
    """
    powerset = []
    for i in range(0, 2**len(items)):
        bin_str = get_binary_rep(i, len(items))
        subset = []
        for j in range(len(items)):
            if bin_str[j] == '1':
                subset.append(items[j])
        powerset.append(subset)
    return powerset



@pytest.fixture
def items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50 , 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for name, value, weight in zip(names, values, weights):
        items.append(Item(name, value, weight))
    return items


def test_get_powerset(items):
    powerset = get_powerset(items)
    print('powerset: {}'.format(powerset))
    print('len(powerset): {}'.format(len(powerset)))
    # 2^6: 6個の荷物それぞれに選ぶ、選ばないという2通りが存在する


def test_choose_best(items):
    max_weight = 20
    pset = get_powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)
    display_items_list(taken, val)
    #itemの名前順が一致しているかで正当判定する
    expected_taken_names = ['clock', 'painting', 'book']
    compare(expected_taken_names, get_item_names_from_list(taken))
    
# pytestの記法に合わせる
# TODO parameterized testへの変更
def test_greedy(items):
    max_weight = 20
    key_function = value
    # 名前だけ確認
    expected_taken_names = ['computer']
    taken, val = greedy(items, max_weight, key_function)
    compare(expected_taken_names, get_item_names_from_list(taken))
    display_items_list(taken, val)

    # key_function: weight_inverse
    key_function = weight_inverse
    expected_taken_names = ['book', 'vase', 'radio', 'painting']
    taken, val = greedy(items, max_weight, key_function)
    compare(expected_taken_names, get_item_names_from_list(taken))
    display_items_list(taken, val)

    key_function = density
    expected_taken_names = ['vase', 'clock', 'book', 'radio']

    taken, val = greedy(items, max_weight, key_function)
    compare(expected_taken_names, get_item_names_from_list(taken))
    display_items_list(taken, val)



