g1 = {
    'A' : ['B','C','F'],
    'B' : ['A','D','J'],
    'C' : ['A','F'],
    'D' : ['B','E','G','H'],
    'E' : ['D','G'],
    'F' : ['H','K'],
    'G' : ['D','E','I','J'],
    'H' : ['D','F','I'],
    'I' : ['G','H','J'],
    'J' : ['B','I','K'],
    'K' : ['F','J']
    }

g2 = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'D'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

def BFS(start_node,graph):
    queue = [start_node]
    visited = [start_node]
    
    while queue:
        now = queue[0]
        
        for i in graph[now]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
        queue.pop(0)
    return visited

# for DFS change queue.append(i) --> queue.insert(0,i)


print(BFS('A',g1))

