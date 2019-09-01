K = int(input())

even = 0
odd = 0
for i in range(K):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("{}".format(even*odd))