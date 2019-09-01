import math

n = int(input())

power = math.factorial(n)

mod = 10**9+7

print(power % mod)