import math, sys

N = int(input())

sqrt_n = round(math.sqrt(N))
# print(sqrt_n)

min_f = sys.maxsize
for i in range(sqrt_n, 0, -1):
    if N % i == 0:
        len_A = len(str(i))
        len_B = len(str(N//i))
        F = max(len_A, len_B)
        min_f = min(min_f, F)

print(min_f)