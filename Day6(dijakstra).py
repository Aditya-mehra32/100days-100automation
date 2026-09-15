import heapq
import math

def dijkstra(n: int, src: int, adj: list[list[tuple[int, int]]]):
    """
    adj[u] = list of (neighbor, weight)
    Returns: (distances, parent pointers)
    """
    dist = [math.inf] * n
    parent = [-1] * n
    dist[src] = 0
    
    # Priority queue stores (current_distance, node)
    pq = [(0, src)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Skip stale entries
        if d > dist[u]:
            continue
            
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
                
    return dist, parent
