g1 = {"A" : ["B","C","F"],
      "B" : ["A","D","J"],
      "C" : ["A","F"],
      "D" : ["B","E","G","H"],
      "E" : ["D","G"],
      "F" : ["H","K"],
      "G" : ["D","E","I","J"],
      "H" : ["D","F","I"],
      "I" : ["G","H","J"],
      "J" : ["B","I","K"],
      "K" : ["F","J"]}

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

def BFS(start_node,end_node,graph):
    queue = [start_node]
    visited = [start_node]
    
    while queue:
        now = queue[0]
        if now == end_node:
            if now not in visited:
                visited.append(now)
            return visited
        
        for i in graph[now]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
        queue.pop(0)

print(BFS("B","K",g1))