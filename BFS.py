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
    visited = {start_node : 0} # { node : lvl }
    
    while queue:
        now = queue[0]
        
        for i in graph[now]:
            if i not in visited.keys():
                visited[i] = visited[now]+1
                print(visited)
                queue.append(i)
                
        queue.pop(0)
    return visited


# lebel tree level (Later)


# Input part
num_nodes = int(input("Total nodes : "))
graph = {}
    
for i in range(num_nodes):
    node = input("node : ")
    connect = [i for i in input("connect to : ").split()]
    graph[node] = connect   
    #print(graph)

start = input("Start from node : ")

# Output part
bfs = BFS('A',g1)
#bfs = BFS(start,graph)
max_lvl = max(bfs.values())

for lvl in range(max_lvl+1):
    level_node = []
    
    for i in bfs:
        if bfs[i] == lvl:
            level_node.append(i)
    
    print(f"Node level {lvl} = {level_node}")