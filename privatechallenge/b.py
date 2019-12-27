import numpy as np

def move_left(row):
    C = len(row)
    # 0詰めの行をつくる
    non_zeros = [xi for xi in row if xi != 0]
    row.fill(0)
    for i, xi in enumerate(non_zeros):
        row[i] = xi

    for i in range(C - 1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            # i+1をつぶす。C-1（最後の要素）を残すことでサイズが小さくならないようにする
            row[i+1:C-1] = row[i+2:]
            # 最後の要素はi+1をつぶしたので0をいれる
            row[C-1] = 0
    return row


def move(X, command):
    if command in ('U', 'D'):
        # DはR,　UはLにとみなす
        # 行列を転置することでそのようにみなせる
        virtual_command = 'R' if command ==  'D' else 'L'
        # N*M行列がM*N行列になるのでMを行数Rとする
        R = M
        X = X.T
    else:
        virtual_command = command
        R = N

    for k in range(R):
        if virtual_command == 'R':
            # 要素の順序を逆順にする
            X[k] = X[k][::-1]

        X[k] = move_left(X[k])

        if virtual_command == 'R':
            # 要素の順序を戻す
            X[k] = X[k][::-1]

    if command in ('U', 'D'):
        X = X.T

    return X


N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

X = np.asarray(X)
s = input()

for si in s:
    X = move(X, si)

for xi in X:
    print(' '.join(map(str, xi)))
