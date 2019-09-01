n = int(input())
k = int(input())

x_list = list(map(int, input().split()))

cost = 0
for x in x_list:
    if x <= k/2:
        cost = cost + 2*x
    else:
        cost = cost + 2*(k-x)
print(cost)

        