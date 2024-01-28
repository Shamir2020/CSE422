# Name - Shamir Roy
# ID - 20241015
# Course - CSE422
# Section - 06

import heapq
file = open('input file.txt','r')

graph = {}
heauristic = {}
for x in file:
    x = x.split(' ')
    head = x[0]
    hr = int(x[1])

    li = []
    for i in range(2,len(x)-1):
        if i%2 == 0:
            t = (x[i], int(x[i+1]))
            li.append(t)

    graph[head] = li
    heauristic[head] = int(x[1])




def AStarSearch(graph, start, goal):
    global heauristic
    op = [(0, start)]
    cs = set()
    path = []
    distance = 0

    g = {}
    f = {}
    for key in graph.keys():
        g[key] = float('inf')
        f[key] = float('inf')

    g[start] = 0

    f[start] = heauristic[start]

    while op:
        a, current = heapq.heappop(op)
        path.append(current)
        
        if current == goal:
            
            distance = calculateDistance(graph, start, goal,path)
            return path , distance
        cs.add(current)
       
        for child, cost in graph[current]:
            if child in cs:
                continue
                
            tg = g[current] + cost

            if tg < g[child]:
                g[child] = tg
                f[child] = g[child] + heauristic[child]
                distance += tg
                heapq.heappush(op, (f[child], child))

    return None, None



def calculateDistance(graph, start, goal, path):
    distance = 0
    head = start

    
    for i in range(len(path)-1):
        node = path[i]
        next = path[i+1]

        d = 0

        for child, cost in graph[node]:
            if child == next:
                distance += cost
                break 

    return distance        
    




path, distance = AStarSearch(graph, 'Arad', 'Bucharest')

if path is not None:
    print('Path : ',end='')
    for i in range(len(path)):
        if i < len(path) - 1:
            print(path[i],end=' => ')
        else:
            print(path[i])

    print(f'Total Distance: {distance} KM')
else:
    print('NO PATH FOUND')