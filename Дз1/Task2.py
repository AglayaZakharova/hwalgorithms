from enum import Enum

class Color(Enum):
    WHITE = 0,
    GRAY = 1,
    BLACK = 2


def has_cycle_dir(g: list[list[int]]) -> bool:
    c = [Color.WHITE]*len(g)
    def dfs(v: int) -> bool:   
        if c[v] % 2 == 0:
            c[v] = Color.BLACK
        else:                 
            c[v] = Color.GRAY
        for u in g[v]:
            if c[u] == Color.GRAY or (c[u] == Color.WHITE and dfs(u)):
                return True
        c[v] = Color.BLACK
        return False
    for v in range(len(g)):
        if c[v] == Color.WHITE and dfs(v):
            return True
    return False