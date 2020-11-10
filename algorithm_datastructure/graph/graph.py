# 12.2 グラフ最適化問題

class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dst):
        """src, dstはどちらもNodeオブジェクト
        """
        self.src = src
        self.dst = dst

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dst

    def __str__(self):
        return self.src.get_name() + '->' + self.dst.get_name()


class WeightedEdge(Edge):
    def __init__(self, src, dst, weight=1.0):
        """src, dstはNodeオブジェクト、weightは数値
        """
        self.src = src
        self.dst = dst
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src.get_name() + '->(' + self.weight + ')' + self.dst.get_name()


class Digraph(object):
    """nodesはNodeオブジェクトのリストである
    edgesは各nodeを、そのnodeの子ノードのリストにマップする辞書
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("duplicate node")
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dst in self.edges:
                result = result + src.get_name() + '->' + dst.get_name() + '\n'
        # 最後の改行を削除
        return result[:-1]


class Graph(Digraph):
    def add_edge(self, edge):
        super().add_edge(edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        super().add_edge(rev)


def print_path(path):
    """pathはNodeオブジェクトからなるリストととする

    Args:
        path ([type]): [description]
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def dfs(graph, start, end, path, shortest, to_print=False):
    """depth-first searh(深さ優先探索)
    graphでのstartからendへの最短経路を返却する。
    再帰的なメソッド

    Args:
        graph (Digraph): [description]
        start (Node): [description]
        end (Node): [description]
        path ([Node]): [description]
        shortest ([Node]): [description]
        to_print (bool, optional): [description]. Defaults to False.
    """
    path = path + [start]

    if to_print:
        print(f'Current DFS path: {print_path(path)}')

    # 再帰的な探索によりゴール(end)まで行き着いたとき
    if start == end:
        return path

    # startノードから次のノードを探索する
    for node in graph.children_of(start):
        # ループを避ける
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path

    return shortest


def shortest_path(graph, start, end, to_print=False):
    return dfs(graph, start, end, [], None, to_print)