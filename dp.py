# http://wakabame.hatenablog.com/entry/2017/09/10/211428
# 2番目の解説をpythonで書いたもの# https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-1%E6%9C%80%E5%A4%A7%E5%92%8C%E5%95%8F%E9%A1%8C

# dp解説を整理したもの．分かりやすい．コードはc++

# 最大和
def max_sum(N, a):
    # N+1次元の配列を作成
    # 少しだけ多めにとる
    dp = [0] * (N + 1)

    for i in range(N):
        # dp[i]にa[i]を追加した場合，しない場合で値が大きい方がdp[i+1]
        dp[i+1] = max(dp[i], dp[i] + a[i])
    return dp[N]


def test_max_sum():
    n = 3
    a = [7, -6, 9]
    print("expected:16 actual:", max_sum(n, a))
    n = 2
    a = [-9, -16]
    print("expected:0 actual:", max_sum(n, a))


# ナップサック問題
def knapsack(N, W, weight, value):
    # 初期化
    print(" N,W:{},{}".format(N, W))
    inf = float("inf")
    # [N+1][W+1]の多次元リストを作成．初期値は最小値
    dp = [[-inf for i in range(W+1)] for j in range(N+1)]
    
    # dp[0][i]は0-1番目までの荷物で重さiを越えない範囲で価値が最大化
    # 0-1(=-1)番目な荷物は存在しないので価値は0
    for i in range(W+1):
        dp[0][i] = 0
    print(" len(dp[0])", len(dp[0]))
    
    # DP
    for i in range(N):
        for w in range(W+1):
            if weight[i] <= w:
                # weight[i]がwより小さいとき
                # w-weight[i]=まだ詰め込める荷物の重さ
                # dp[i][w]の方が価値が高くなるなんてことあるか？
                # -> ありえる．[w-weight[i]]の制約下で選んだものよりも，w制約下で選んだ方が価値が高い場合ということ
                dp[i+1][w] = max(dp[i][w-weight[i]]+value[i], dp[i][w])
            else: # i番目の荷物を選ばない場合
                dp[i+1][w] = dp[i][w]
    return dp[N][W]

# 部分和数え上げ問題
def part_sum(a,A):
    """
    制約
    1 <= n <= 100
    1 
    """
    p=10**9+7
    #初期化
    N=len(a)
    dp=[[0 for i in range(A+1)] for j in range(N+1)]
    dp[0][0]=1

    #DP
    for i in range(N):
        for j in range(A+1):
          if a[i]<=j: #i+1番目の数字a[i]を足せるかも
            dp[i+1][j]=dp[i][j-a[i]]+ dp[i][j]% p
          else: #入る可能性はない
            dp[i+1][j]=dp[i][j]%p
    return dp[N][A]

def test_knapsack():
    print("test knapsack")
    N = 4
    W = 5
    value = [4, 5, 2, 8]
    weight = [2, 2, 1, 3]
    print("expected:13 actual:", knapsack(N, W, weight, value))

if __name__ == '__main__':
    test_max_sum()
    test_knapsack()