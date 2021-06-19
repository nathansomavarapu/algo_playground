from collections import deque, defaultdict
def bfs(start: int, V: list, E: list) -> dict:
    
    q = deque([start])
    visited = set()
    adj = defaultdict(list)
    dist = {start:0}
    
    for u,v in E:
        adj[u].append(v)

    while len(q) != 0:
        curr = q.popleft()

        for u in adj[curr]:
            if u not in visited:
                q.append(u)
                dist[u] = dist[curr] + 1
        
            visited.add(curr)
    
    return dist


E = [
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (5,6),
    (6,2)
    ]

dists = bfs(1, list(range(1,6)), E)
print(dists)