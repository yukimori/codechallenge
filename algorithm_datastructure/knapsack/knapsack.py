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

def greedy(items, max_weight, key_function):
    """itemsはリスト、max_weight>=0とする
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


@pytest.fixture
def items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50 , 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for name, value, weight in zip(names, values, weights):
        items.append(Item(name, value, weight))
    return items


def get_item_names_from_list(items_list):
    """
    itemのリストから名前リストだけ取り出す
    """
    names = []
    for item in items_list:
        names.append(item.get_name())
    return names


def display_items_list(items, val):
    print('Total valud of items taken is ', val)
    for item in items:
        print(' ', item)    


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



