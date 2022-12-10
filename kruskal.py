g1 = {
        2 : [['S','A'],['A','B'],['C','B'],['E','T']],
        3 : [['S','C'],['B','D'],['F','E']],
        4 : [['F','T']],
        5 : [['S','B']],
        6 : [['B','F'],['A','D'],['D','T']],
        7 : [['C','F']]
       }

g2 = {
        1 : [['A','B']],
        2 : [['A','C'],['C','F'],['F','H'],['F','J']],
        3 : [['A','D'],['B','C'],['E','F'],['F','G'],['F','I'],['I','K']],
        4 : [['D','F'],['B','E'],['E','H'],['H','K'],['I','J'],['J','K']],
        5 : [['C','D'],['B','F'],['D','G'],['H','I']]
}

def kruskal(graph):
       weight = [i for i in graph.keys()]
       visited = []
       total_w = 0
       while weight:
              current_weight = weight[0]
              
              for i in graph[current_weight]:
                     
                     if (i[0] not in visited) and (i[1] not in visited):
                            visited.append(i[0])
                            visited.append(i[1])
                            total_w += current_weight
                            continue
                     
                     if i[0] not in visited:
                            visited.append(i[0])
                            total_w += current_weight
                            
                     if i[1] not in visited:
                            visited.append(i[1])
                            total_w += current_weight
                     
              weight.pop(0)
       return visited, total_w

path, weight_sum = kruskal(g2)
print(path)
print(weight_sum)
