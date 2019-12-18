"""
https://atcoder.jp/contests/abc124/tasks/abc124_c

ef:http://drken1215.hatenablog.com/entry/2019/04/14/174800

隣が異なる色にする必要がある
色は2種類なので１つがきまると連鎖的に他も決まる
白黒白黒...
黒白黒白...
という２つのパターンしかない
"""

def solve4():
    s = list(input())

    s_len = len(s)

    # s_lenが奇数のときを考慮しなければならない
    if s_len % 2 == 0:
        case1 = "10" * (s_len // 2)
        case2 = "01" * (s_len // 2)
    else:
        case1 = "10" * (s_len // 2) + "1"
        case2 = "01" * (s_len // 2) + "0"

    case1_num = 0
    case2_num = 0
    # s_list = list(s)
    # case1_list = list(case1)
    # case2_list = list(case2)
    for s_char, case1_char, case2_char in zip(s, case1, case2):
        if s_char != case1_char:
            case1_num += 1
        if s_char != case2_char:
            case2_num += 1

    return min(case1_num, case2_num)
        

def solve3():
    """solve1の変形
    ２種類のパターンしかないので分岐して調べる
    """
    S = list(input())
    c1, c2 = 0, 0
    for i in range(len(S)):
        # 正解を1010...とした場合
        if i % 2 == 0 and S[i] == '0':
            c1 += 1
        if i % 2 == 1 and S[i] == '1':
            c1 += 1
        # 正解を0101...とした場合
        if i % 2 == 0 and S[i] == '1':
            c2 += 1
        if i % 2 == 1 and S[i] == '0':
            c2 += 1
    return(min(c1, c2))

def solve2():
    l = list(str(input()))
    l = [int(i) for i in l]
    cnt = 0
    # チェックをしたのち次のものを適切な色に変更する
    # 全てのタイルに適用することで間違いをカウントすることができる
    for i in range(len(l)-1):
        if(l[i]==l[i+1]):
            cnt+=1
        if(l[i]==0):
            l[i+1]=1
        elif(l[i]==1):
            l[i+1]=0
    return cnt

def solve1():
    s = input()
    n = len(s)
 
    counter_bw = 0
    counter_wb = 0
    
    # 指定された長さに従って正解の文字列を作ってしまう
    if n % 2 == 0:
        bw = "01" * (n // 2)
        wb = "10" * (n // 2)
    else:
        bw = "01" * (n // 2) + "0"
        wb = "10" * (n // 2) + "1"
    
    # 作成した正解文字列と違うところを比較
    for i in range(n):
        if s[i] != bw[i]:
            counter_bw += 1
        if s[i] != wb[i]:
            counter_wb += 1

    # 2種類しかないので違いが少ないほうの違いの数を示せばいい
    return min(counter_bw, counter_wb)

# print(solve1())
# print(solve2())
print(solve4())