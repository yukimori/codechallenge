from itertools import accumulate

N, K = map(int, input().split())
a = list(map(int, input().split()))

# 部分数列の和を計算
s = [x for x in accumulate(a)]

ans = 0
for i in range(0, N-K+1):
    if i == 0:
        ans += s[i+K-1]
    else:
        ans += s[i+K-1] - s[i-1]
print(ans)

""" 計算量がO(n^2)になるためTLEになる
for i in range(0, N-K+1):
    # print(a[i:i+K])
    s += sum(a[i:(i+K)])
 """
