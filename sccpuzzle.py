n, m = list(map(int, input().split()))

num_without_s = m/4
num_with_s = 0
m_tmp = m
n_tmp = n
""" while m_tmp > 1 and n_tmp > 0:
    num_with_s += 1
    m_tmp = m_tmp - 2
    n_tmp = n_tmp - 1
 """

if m >= (2 * n):
    num_with_s = n
    if (m_tmp - 2*n) > 3:
        num_with_s = num_with_s + int(((m_tmp - 2*n) / 4))
else:
    num_with_s = int(m/2)

if num_with_s > num_without_s:
    print(int(num_with_s))
else:
    print(int(num_without_s))
    