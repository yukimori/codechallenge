import time, sys, os
import unittest
import contextlib
import pytest
from testfixtures import compare, Comparison as C

from .graph import Node

# importを有効にするには__init__.pyを配置する必要あり
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithm_datastructure_util import time_measure

@pytest.fixture
def test_digraph():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))

    

    