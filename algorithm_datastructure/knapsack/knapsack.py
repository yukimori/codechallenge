from item import Item


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


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50 , 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for name, value, weight in zip(names, values, weights):
        items.append(Item(name, value, weight))
    return items
