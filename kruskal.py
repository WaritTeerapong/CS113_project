g1 = {
        2 : [['S','A'],['A','B'],['C','B'],['E','T']],
        3 : [['S','C'],['B','D'],['D','E'],['F','E']],
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
       weight = [i for i in graph.keys()] #like queue
       visited = []
       total_w = 0
       while weight:
              current_weight = weight[0]
              
              for i in graph[current_weight]:
                     
                     
                     append_check = False
                     for j in range(len(visited)):
                            
                            if i[1] in visited[j] and i[0] in visited[j]:
                                   append_check = True
                                   break
                            
                            if i[0] in visited[j] and i[1] not in visited[j]:
                                   visited[j].append(i[1])
                                   total_w += current_weight
                                   append_check = True
                                   break
                            elif i[1] in visited[j] and i[0] not in visited[j]:
                                   visited[j].append(i[0])
                                   total_w += current_weight
                                   append_check = True
                                   break
                     if not append_check :
                            visited.append(i)
                            total_w += current_weight
                     
                     # check connect of different node group
                     visited.sort(reverse = True, key = lambda x:len(x)) # main group node (longest) is at visited[0]
                     for small_group in range(1,len(visited)):
                            
                            for node in visited[small_group]:
                                   if node in visited[0]:
                                          visited[small_group].remove(node) #remove replication node
                                          
                                          visited[0].append(*visited[small_group]) # append the rest node to the main group
                                          
                                          visited.remove(visited[small_group]) # remove smaller group node
                                          break
                            
                                 
                     print(visited)
                     print(total_w)
              weight.pop(0)
       return visited, total_w

path, weight_sum = kruskal(g1)
print(path)
print(weight_sum)
