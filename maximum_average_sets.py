import math
import functools
N, A, B = map(int, input().split())
V = sorted([int(x) for x in input().split()], reverse=True)
print(sum(V[:A]) / A)
threshold = V[:A][-1]
fixed = 0
chosen = 0
for v in V:
  if v > threshold:
    fixed += 1
  elif v == threshold:
    chosen += 1
def nCn(a, b):
  return math.factorial(a) // math.factorial(b) // math.factorial(a - b)
if fixed:
  print(nCn(chosen, A - fixed))
else:
  count = 0
  for i in range(A, min(B, chosen) + 1):
    count += nCn(chosen, i)
  print(count)


def other_solv():
    from math import factorial
    N, A, B = map(int, input().split())
    v = [int(vi) for vi in input().split()]
    
    def combination(n, r):
        return factorial(n) // (factorial(n - r) * factorial(r))
    
    v = sorted(v, reverse=True)
    basket = v[:A]
    max_basket = basket[0]
    min_basket = basket[-1]
    print(sum(basket) / len(basket))
    
    n_selected = 0
    n_candidate = 0
    for vi in v:
        if vi > min_basket:
            n_selected += 1
        elif vi == min_basket:
            n_candidate += 1
    
    if min_basket != max_basket:
        print(combination(n_candidate, A - n_selected))
    else:
        count = 0
        for i in range(A, min(B, n_candidate) + 1):
            count += combination(n_candidate, i)
        print(count)
