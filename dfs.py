from collections import defaultdict, deque
from typing import Tuple

class DFS:

    def __init__(self, vertices: list, edges: list) -> None:
        self.visited = set()
        self.neighbors = self._generate_adj_dict(edges)
        self.previsit = {}
        self.vert_to_postvisit = {}
        self.postvisit_to_vert = {} # Used for bucket sort for linear time
        self.clock = 1

        self.vertices = vertices
        self.n = len(vertices)
        self.edges = edges
        self.ts = []

    def explore(self, vertex: int, ts: bool) -> None:
        if vertex in self.visited:
            return
        
        self.previsit[vertex] = self.clock
        self.clock += 1

        self.visited.add(vertex)

        for u in self.neighbors[vertex]:
            if ts and (u not in self.vert_to_postvisit and u in self.previsit):
                raise ValueError('Cycle Detected')
            self.explore(u, ts)

        self.postvisit_to_vert[self.clock] = vertex
        self.vert_to_postvisit[vertex] = self.clock
        self.clock += 1

    def _generate_adj_dict(self, edges: list) -> dict:
        neighbors = defaultdict(list)
        for u,v in edges:
            neighbors[u].append(v)

        return neighbors

    def recursive_dfs(self, ts: bool = False) -> Tuple[dict,dict]:

        for n in self.vertices:
            if n not in self.visited:
                self.explore(n, ts)

        return self.previsit, self.vert_to_postvisit

    def topological_sort(self) -> list:
        if len(self.vert_to_postvisit) != self.n:
            self.recursive_dfs(ts=True)
        for pv in range(2*self.n, 0, -1):
            if pv in self.postvisit_to_vert:
                self.ts.append(self.postvisit_to_vert[pv])
        
        return self.ts
    
    def iterative_dfs(self, ts: bool = False) -> Tuple[dict, dict]:
        s = deque()
        
        for v in self.vertices:
            if v not in self.visited:
                self.explore_it(v, ts)
        
        return self.previsit, self.vert_to_postvisit

    def explore_it(self, vertex: int, ts: bool) -> None:
        s = deque()
        s.append(vertex)
        
        self.visited.add(vertex)
        self.previsit[vertex] = self.clock
        self.clock += 1

        while len(s) != 0:
            curr = s[-1]
            unvisited = False
            for u in self.neighbors[curr][::-1]:
                if u not in self.visited:
                    self.previsit[u] = self.clock
                    self.clock += 1
                    self.visited.add(u)
                    s.append(u)
                    unvisited = True
            
            if not unvisited:
                s.pop()
                self.vert_to_postvisit[curr] = self.clock
                self.postvisit_to_vert[self.clock] = curr
                self.clock += 1

V = [1,2,3,4,5,6]
# E = [
#     (2,1),
#     (3,2),
#     (4,3),
#     (5,4),
#     (6,5)
#     ]

E = [
    (1,2),
    (1,3),
    (3,4),
    (4,5),
    (5,6),
    (6,2)
    ]

# E = [
#     (1,2),
#     (2,3),
#     (3,4),
#     (4,5),
#     (5,6),
#     ]

dfs = DFS(V, E)
pre_rec, post_rec = dfs.recursive_dfs()
dfs = DFS(V, E)
pre_it, post_it = dfs.iterative_dfs()

print(pre_rec)
print(pre_it)
print(post_rec)
print(post_it)

print(pre_rec == pre_it)
print(post_rec == post_it)
