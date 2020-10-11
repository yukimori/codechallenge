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