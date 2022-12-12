
import math
# g1 = { "S" : {"A":2,"B":5,"C":3},
#           "A" : {"S":2,"B":2,"D":6},
#           "B" : {"S":5,"A":2,"C":2,"D":3,"F":6},
#           "C" : {"S":3,"B":2,"F":7},
#           "D" : {"A":6,"B":3,"E":3,"T":6},
#           "E" : {"D":3,"F":3,"T":2},
#           "F" : {"B":6,"C":7,"E":3,"T":4},
#           "T" : {"D":6,"E":2,"F":4}
#         }

g1 = { "a" : {"b":4,"h":8},
          "b" : {"a":4,"c":8,"h":11},
          "c" : {"b":8,"i":2,"f":4,"d":7},
          "d" : {"c":7,"f":14,"e":9},
          "e" : {"d":9,"f":10},
          "f" : {"d":14,"c":4,"g":2,"e":10},
          "g" : {"f":2,"i":6,"h":1},
          "h" : {"a":8,"i":7,"g":1},
          "i" : {"c":2,"h":7,"g":6}
        }

def dijkstra(start,end):
    node = {i: [math.inf,""] for i in g1}
    # print(node)
    node[start] = [0,""]
    visited = []
    path = [end]
    queue = [start]
    while queue:
        for i in g1[queue[0]]:
            if i not in visited and g1[queue[0]][i] + node[queue[0]][0] < node[i][0]:
                node[i][0] = g1[queue[0]][i] + node[queue[0]][0]
                node[i][1] = queue[0]
                queue.append(i)
        visited.append(queue[0])
        queue.pop(0)

    track = end
    while start not in path:
        path.append(node[track][1])
        track = node[track][1]

    return node[end][0], path[::-1]
    
start = 'a'
end = 'e'
distance, path = dijkstra(start,end)
print("Distance :",distance)
print("Path :",end="")
for i in path:
    print(i,end=" ")
print()