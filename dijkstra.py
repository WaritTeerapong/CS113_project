g1 = { "S" : {"A":2,"B":5,"C":3},
          "A" : {"S":2,"B":2,"D":6},
          "B" : {"S":5,"A":2,"C":2,"D":3,"F":6},
          "C" : {"S":3,"B":2,"F":7},
          "D" : {"A":6,"B":3,"E":3,"T":6},
          "E" : {"D":3,"F":3,"T":2},
          "F" : {"B":6,"C":7,"E":3,"T":4},
          "T" : {"D":6,"E":2,"F":4}
        } 
    




def shortest_path(start,end,table):
    pass

def dji_table(start,end,graph):
    node_min = {i: 999999 for i in g1} # {'S': 999999, 'A': 999999, 'B': 999999, 'C': 999999, 'D': 999999, 'E': 999999, 'F': 999999, 'T': 999999}
    node_min[start] = 0 
    unvisited = [i for i in node_min] # ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'T']
    
    while unvisited:
        pass
