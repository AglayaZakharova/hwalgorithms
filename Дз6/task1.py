import sys
from collections import deque

# сначала сделаем класс для сети
class FlowGraph:
    def __init__(self, n):
        self.sz = n
        self.buffer = [0] * (n * n)

    def add_flow(self, x, y, delta):
        self.buffer[self.sz * x + y] += delta

    def set_flow(self, x, y, delta):
        self.buffer[self.sz * x + y] = delta

    def get_flow(self, x, y):
        return self.buffer[self.sz * x + y]

    def size(self):
        return self.sz


def fix_way(graph, flow, s, t, parent):
    cur = t
    delta = -1
    while cur != s:
        max_flow_for_edge = graph.get_flow(parent[cur], cur) - flow.get_flow(parent[cur], cur)
        delta = max_flow_for_edge if delta == -1 else min(max_flow_for_edge, delta)
        cur = parent[cur]
    cur = t
    while cur != s:
        flow.add_flow(parent[cur], cur, delta)
        flow.add_flow(cur, parent[cur], -delta)
        cur = parent[cur]
    return delta


def up_flow(graph, flow, s, t):
    parent = [-1] * graph.size()
    used = [False] * graph.size()
    q = deque([s])
    used[s] = True
    while q:
        v = q.popleft()
        if v == t:
            return fix_way(graph, flow, s, t, parent)
        for i in range(graph.size()):
            max_flow = graph.get_flow(v, i)
            cur_flow = flow.get_flow(v, i)
            if not used[i] and max_flow - cur_flow > 0:
                parent[i] = v
                used[i] = True
                q.append(i)
    return 0


def edmonds_karp(g, s, t):
    res = 0
    delta = 0
    f = FlowGraph(g.size())
    while True:
        delta = up_flow(g, f, s, t)
        if delta == 0:
            break
        res += delta
    return res


def make_graph(n, m):
    inf = 100000000
    guess_max = 0
    g = FlowGraph(n + m + 2)
    for t in range(1, m + 1):
        cnt = int(sys.stdin.readline())
        guess_max += cnt
        g.add_flow(0, t, cnt)
    guess_max //= n
    for i in range(1, n + 1):
        cnt = int(sys.stdin.readline())
        for j in range(cnt):
            t = int(sys.stdin.readline())
            g.add_flow(t, m + i, inf)
    return g, guess_max


def get_day_num(graph, n, m, guess_max):
    c = FlowGraph(graph.size())
    c.buffer = graph.buffer[:]
    left = 0
    right = guess_max + 1
    while right - left > 1:
        mid = (right + left) // 2
        for i in range(1, n + 1):
            c.set_flow(m + i, n + m + 1, mid)
        if edmonds_karp(c, 0, n + m + 1) == mid * n:
            left = mid
        else:
            right = mid
    return left


# решаем
n, m = map(int, input().split()) # n - количество людей, m - количество чайных пакетиков
graph, guess_max = make_graph(n, m)
print("Result =", get_day_num(graph, n, m, guess_max))

