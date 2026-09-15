import math

def bellman_ford(n: int, src: int, edges: list[tuple[int, int, int]]):
    """
    edges = list of (u, v, weight)
    Returns: (distances, parent pointers, has_negative_cycle)
    """
    dist = [math.inf] * n
    parent = [-1] * n
    dist[src] = 0
    
    # Relax edges up to (n - 1) times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break
            
    # Detect reachable negative-weight cycle
    has_negative_cycle = any(
        dist[u] != math.inf and dist[u] + w < dist[v]
        for u, v, w in edges
    )
    
    return dist, parent, has_negative_cycle
