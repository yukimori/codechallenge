import time, sys, os
import unittest
import contextlib
import pytest
from testfixtures import compare, Comparison as C

from .graph import Node
from .graph import Digraph
from .graph import Edge

# importを有効にするには__init__.pyを配置する必要あり
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithm_datastructure_util import time_measure

@pytest.fixture
def test_digraph():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))

    g = Digraph()
    for n in nodes:
        g.add_node(n)

    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    
    return {'g': g, 'nodes' : nodes}
    

def test_SP(test_digraph):
    from .graph import shortest_path
    from .graph import print_path
    sp =  shortest_path(test_digraph['g'], test_digraph['nodes'][0], 
                            test_digraph['nodes'][5], to_print=True)
    assert print_path(sp) == '0->2->3->5'
    print(f"shortest path found by DFS: {print_path(sp)}")