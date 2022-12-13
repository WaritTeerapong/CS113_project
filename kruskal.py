'''
       65090500409 ฑีฆมล ชัยวงศ์วุฒิกุล
       65090500424 วริศ   ธีระพงษ์
       65090500432 ชัยธวัช สะกลาง
'''

# g1 = {
#         2 : [['S','A'],['A','B'],['C','B'],['E','T']],
#         3 : [['S','C'],['B','D'],['F','E'],['D','E']],
#         4 : [['F','T']],
#         5 : [['S','B']],
#         6 : [['B','F'],['A','D'],['D','T']],
#         7 : [['C','F']]
#        }

g2 = {
        1 : [['A','B']],
        2 : [['A','C'],['C','F'],['F','H'],['F','J']],
        3 : [['A','D'],['B','C'],['E','F'],['F','G'],['F','I'],['I','Z']],
        4 : [['D','F'],['B','E'],['E','H'],['H','Z'],['I','J'],['J','Z'],['G','J']],
        5 : [['C','D'],['B','F'],['D','G'],['H','I']]
}


def kruskal(graph):
       weight = [i for i in graph.keys()] #like queue
       visited = []
       total_w = 0
       while weight:
              current_weight = weight[0]
              
              for i in graph[current_weight]: 
                     
                     for j in range(len(visited)):
                            
                            # break loop when both are visited
                            if i[1] in visited[j] and i[0] in visited[j]: 
                                   break
                            # append only one node that haven't visited
                            if i[0] in visited[j] and i[1] not in visited[j]:
                                   visited[j].append(i[1])
                                   total_w += current_weight
                                   break
                            elif i[1] in visited[j] and i[0] not in visited[j]:
                                   visited[j].append(i[0])
                                   total_w += current_weight
                                   break
                            
                     # add both nodes that haven't visited yet      
                     else: 
                            visited.append(i)
                            total_w += current_weight
                     
                     # check connection of different node group
                     visited.sort(reverse = True, key = lambda x:len(x)) # main group node (longest) is at visited[0]
                     for small_group in range(1,len(visited)):
                            
                            for node in visited[small_group]:
                                   if node in visited[0]:
                                          visited[small_group].remove(node) #remove replication node
                                          
                                          for i in visited[small_group]:
                                                 visited[0].append(i) # append the rest node to the main group
                                          
                                          visited.remove(visited[small_group]) # remove smaller group node
                                          break
                            
                     print(visited)
                     print(total_w)
              weight.pop(0)
       return visited, total_w

# Input part
edge = int(input("How many edges : "))
graph = {}

for i in range(edge):
       print(graph)
       node = [ i for i in input("nodes connected : ").split()]
       weight = int(input("weight : "))
       
       if weight not in graph.keys():
              graph[weight] = [node]
              continue
       
       graph[weight].append(node)

graph = dict(sorted(graph.items())) # sorted weight in graph
print(graph)       

# Output part

path, weight_sum = kruskal(g2)
print(path)
print(weight_sum)
