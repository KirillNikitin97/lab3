n = 8

a, b, c, d, e, f, g, h = range(8)
adj_list = [
	[b, c], # a
	[d, e], # b
	[f, g], # c
	[], # d
	[], # e
	[], # f
	[h], # g
    []
]

s = 0

visited = [False] * n  # массив "посещена ли вершина?"

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if len(adj_list[w]) == 0:
            print(w)
        dfs(w)

dfs(s)
