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
    edgesは
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
        return self.nodes[node]

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