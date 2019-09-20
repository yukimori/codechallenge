"""
n q
name1 time1
name2 time2
...
nameN timeN

n: プロセス数
q: クオンタム（CPUの最大処理時間）
name: プロセス名
time: 必要な処理時間
"""

class Process:
    def __init__(self, name, t):
        self.name = name
        self.t = t


class RingBuffer:

    def __init__(self, processes):
        self.LEN = 100005
        self.MAX = 1000
        self.Q = processes
        self.head = 0
        self.tail = len(processes)

    def initialize(self):
        self.head = 0
        self.tail = 0
        return (self.head, self.tail)


    def is_empty(self):
        return self.head == self.tail


    def isFull(self):
        # MAX:8, tail:7ならhead:0で満杯
        return self.head == (self.tail + 1) % self.MAX


    def enqueue(self, x):
        if self.isFull():
            print("error")
        self.Q.append(x)
        self.tail = (self.tail + 1) % self.LEN


    def dequeue(self):
        if self.is_empty():
            print("cannot dequeue!!!")
        x = self.Q[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x


def min(a, b):
    return a if a < b else b


def resolve2(processes, n, q):
    """リングバッファを使用
    """
    ring = RingBuffer(processes)
    elaps = 0
    while not ring.is_empty():
        u = ring.dequeue()
        # q or u.tだけ処理を行う
        c = min(q, u.t)
        # 残りの必要時間を計算
        u.t -= c
        # 経過時間に加算   
        elaps += c
        if u.t > 0:
            ring.enqueue(u)
        else:
            print("{} {}".format(u.name, elaps))



def resolve1(process, n, q):
    """
    自分で書いたやつ
    listは条件文では要素があるとTrue，空だとFalseを返却する
    """
    complete_process = []
    if process:
        print("process is True")

    elapsed_time = 0
    while process:
        name, time = process.pop(0)
        print("pop:", name, ":", time)
        if time <= q:
            elapsed_time += time
            complete_process.append((name, elapsed_time))
        else:
            process.append((name, (time-q)))
            elapsed_time += q

        print(elapsed_time, ":", process)
    for elem in complete_process:
        print(elem[0], " ", elem[1])
    

def main2():
    """resolve2を使う
    """
    # 入力情報の取得
    n, q = map(int, input().split())
    print(n, q)
    pp = []
    for _ in range(n):
        name, time = input().split()
        p = Process(name, int(time))
        pp.append(p)

    resolve2(pp, n, q)


def main1():
    """resoleve1を使う
    """    
    # 入力情報の取得
    n, q = map(int, input().split())
    print(n, 1)
    
    process = []
    process_info = {}
    for _ in range(n):
        name, time = input().split()
        process.append((name, int(time)))
        process_info[name] = time

    print(process)
    print(type(process[0][0]), type(process[0][1]))
    resolve1(process, n, q)


if __name__ == "__main__":
    # main1()
    main2()
