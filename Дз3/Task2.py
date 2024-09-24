def numOfMinutes(self, n, headID, manager, informTime) -> int:
        d = dict()
        for i in range(n):
            if manager[i] != -1:
                if manager[i] not in d:
                    d[manager[i]] = []
                d[manager[i]].append(i)

        # Идем вглубь, считаем время
        def dfs(node):
            max_time = 0
            for child in d.get(node, []):
                max_time = max(max_time, dfs(child) + informTime[node])
            return max_time

        return dfs(headID)
