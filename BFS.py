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

def BFS(start_node,end_node,graph):
    queue = [start_node]
    visited = [start_node]
    
    while queue:
        now = queue[0]
        if now == end_node:
            visited.append(now)
            return visited
        
        for i in graph[now]:
            if i in visited:
                continue
            queue.append(i)
            visited.append(i)
        queue.pop(0)

print(BFS("A","K",g1))