from typing import List
import heapq
import sys

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def constructAdj(edges, V):
            adj = [[] for _ in range(V)]
            for u, v, wt in edges:
                adj[u].append([v, wt])
                adj[v].append([u, wt])
            return adj

        def dijkstra(V, adj, src):
            dist = [sys.maxsize] * V
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                curr_dist, u = heapq.heappop(pq)
                if curr_dist > dist[u]:
                    continue
                for v, wt in adj[u]:
                    if dist[v] > dist[u] + wt:
                        dist[v] = dist[u] + wt
                        heapq.heappush(pq, (dist[v], v))
            return dist

        adj = constructAdj(edges, n)
        min_count = float('inf')
        result_city = -1

        for i in range(n):
            dist = dijkstra(n, adj, i)
            count = sum(1 for j in range(n) if i != j and dist[j] <= distanceThreshold)
            
            # If two cities have the same count, choose the city with the larger index
            if count <= min_count:
                min_count = count
                result_city = i

        return result_city
