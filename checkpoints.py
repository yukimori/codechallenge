import sys
N, M = list(map(int, input().split()))

ab = [[int(i) for i in input().split()] for i in range(N)]
cd = [[int(i) for i in input().split()] for i in range(M)]

# print("ab:", ab)
# print("cd:", cd)

for i, (a, b) in enumerate(ab):
    # print(i, " ", a, " ", b)
    min_dis = sys.maxsize
    min_idx = -1
    # print(min_idx, " ", min_dis)
    for j, (c, d)  in enumerate(cd):
        distance = abs(a-c) + abs(b-d)
        # print(j, " ", distance)
        if distance < min_dis:
            min_dis = distance
            min_idx = j
    print(min_idx+1)