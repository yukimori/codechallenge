import re

def solve1():
    N, Q = map(int, input().split())
    # print(N, Q)
    acgt_string = input()
    sub_str_ith = []
    for _ in range(Q):
        start, end = map(int, input().split())
        sub_str_ith.append((start, end))

    t = [0] * (N+1)
    for i in range(N):
        print(i)
        t[i+1] = t[i] + (1 if acgt_string[i:i+2] == "AC" else 0)

    for start, end in sub_str_ith:
        print(t[end-1] - t[start-1])

def my_solve1():
    N, Q = map(int, input().split())
    # print(N, Q)
    acgt_string = input()
    sub_str_ith = []
    for _ in range(Q):
        start, end = map(int, input().split())
        sub_str_ith.append((start, end))
    # print(sub_str_ith)

    # 全ての'A'の位置を取得
    a_iths = [m.span() for m in re.finditer('AC', acgt_string)]
    # print(a_iths)

    for start, end in sub_str_ith:
        # print(start, end)
        num = 0
        for ac_start, ac_end in a_iths:
            if ac_start >= start-1 and ac_end <= end:
                num += 1
        print(num)


solve1()
# my_solve1()