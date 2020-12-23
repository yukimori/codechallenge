"""
時刻tにおける価格Rt
Rj-Ri (j>i)の最大値を求める
n 個数
Rt (t=0,1,2,...,n-1)
"""

def solve1():
    """
    Rjのときの最大値を求めるにはjよりも左側の最小値を求める必要あり
    各jで行うとO(n^2)の計算量が必要
    jを増やす過程でそれ以前のRjの最小値を保持しておくことでO(n)の計算量に改善
    """
    minv = rt[0]
    # Rt <= 10^9から？
    maxv = -200000000
    for j in range(1, len(rt)):
        maxv = max(maxv, rt[j]-minv)
        minv = min(minv, rt[j])
    return maxv


if __name__ == '__main__':
    n = int(input())
    rt = []
    for _ in range(n):
        rt.append(int(input()))

    print(solve1())
