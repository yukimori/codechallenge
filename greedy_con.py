# 以下のような入力を想定
# コインの数
# A
coin_nums = list(map(int, input().split()))
coins = [1, 5, 10, 50, 100, 500]
print(coin_nums, coins)
a = int(input())
print(a)

def solve(a):
    ans = 0
    for coin_value, coin_num in zip(coins[::-1], coin_nums[::-1]):
        print(coin_value, coin_num)
        t = int(min((a/coin_value), coin_num))
        a -= int(t * coin_value)
        print("a=", a, "t=", t)
        ans += t
    print("ans=", ans)
    return ans

solve(a)
