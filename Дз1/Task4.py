class Solution(object):
    def findJudge(self, n, trust):
        # Кому доверяют
        in_degree = {i: 0 for i in range(1, n + 1)}
        # Кто доверяет
        out_degree = {i: 0 for i in range(1, n + 1)}

        for a, b in trust:
            out_degree[a] += 1 # Человек кому-то доверяет
            in_degree[b] += 1   # Этому человеку кто-то доверяет

        judge = -1 # Ищем судью
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                judge = i
                break

        return judge
        