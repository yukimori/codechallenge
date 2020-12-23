"""
逆ポーランド記法を演算する
式に含まれるオペランド数　2 <= x <= 100
式に含まれる演算子数 1 <= y <= 99
演算子は+,-,*
1つのオペランドは10^6以下の整数
-1 * 10^9 <= z <= 10^9
"""

formula1 = list(input().split())
print(formula1)

stack = []

ans = 0
for elem in formula1:
    if elem == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
    elif elem == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)
    elif elem == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else:
        stack.append(int(elem))
print(stack.pop())