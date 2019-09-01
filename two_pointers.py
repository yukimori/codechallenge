"""
しゃくとり法
https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
"""

# 単純な総当たり法 O(n^2)
# 入力例
# 6 12
# 5,3,8,6,1,4

# n:aの要素数, x:総和がx以下になるという条件の数値
n, x = map(int, input().split())
print(n, x)
# 数列
a = [int(i) for i in input().split(",")]
print(a)

res = 0
for left, value in enumerate(a):
    sum = 0
    right = left
    while right < n and sum + a[right] <= x:
        sum = sum + a[right]
        right = right + 1

    res = res + (right - left)

print(res)