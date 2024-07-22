#BFS
def enqueue(s,val):
    q.append((val,s))
    return q
def heuristic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d
def empty_tile(mat):
  for i in range(3):
    for j in range(3):
      if mat[i][j]==0:
        return([i,j])
def move_up(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=0:
    mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_down(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=2:
    mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_left(mat):
  l=empty_tile(mat)
  i=l[0]
  j=l[1]
  mat1=copy.deepcopy(mat)
  if j!=0:
    mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
    return mat1
  else:
    return mat
def move_right(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if j!=2:
    mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
    return mat1
  else:
    return mat
def deque():
  global q
  new=[]
  for each in q:
    new.append(each[1])
  new.sort()
  for each in q:
    if(each[1]==new[0]):
      elem=each[0]
      print("elem",elem)
      break
  q.remove((elem,each[1]))
  return ((elem,q))
def bestfs_search(mat,g):
  global q
  global visited
  visited=[]
  q=[]
  visited.append(mat)
  while(1):
      new = move_up(mat)
      val=heuristic(new,g)
      if new != mat:
        if new == g:
            print ("found")
            return
        else:
          if new not in visited:
            q.append((new,val))

      new = move_down(mat)
      val=heuristic(new,g)
      if new != mat:
        if new == g:
          print ("found")
          return
        else:
          if new not in visited:
            q.append((new,val))
      new = move_right(mat)
      val=heuristic(new,g)
      if new != mat:
        if new == g:
          print ("Found")
          return
        else:
          if new not in visited:
            q.append((new,val))
      new = move_left(mat)
      val=heuristic(new,g)
      if new != mat:
        if new == g:
          print ("Found")
          return
        else:
          if new not in visited:
            q.append((new,val))
            print(new)
      if len(q) > 0:
        t = deque()
        mat=t[0]
        q=t[1]
        if mat not in visited:
          visited.append(mat)
      else:
        print ("not found")
import copy
global q
global visited
s=[[1,0,2],[3,4,6],[8,5,7]]
g=[[8,5,3],[7,0,6],[1,4,2]]
bestfs_search(s,g)



#HILL CLIMBING
import copy
def empty_tile(mat):
  for i in range(3):
    for j in range(3):
      if mat[i][j]==0:
        return([i,j])
def heuristic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d
def deque():
  global q
  new=[]
  for each in q:
    new.append(each[1])
  new.sort()
  for each in q:
    if(each[1]==new[0]):
      elem=each[0]
      print("elem",elem)
      break
  q.remove((elem,each[1]))
  return ((elem,q))
def move_up(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=0:
    mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_down(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=2:
    mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_left(mat):
  l=empty_tile(mat)
  i=l[0]
  j=l[1]
  mat1=copy.deepcopy(mat)
  if j!=0:
    mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
    return mat1
  else:
    return mat
def move_right(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if j!=2:
    mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
    return mat1
  else:
    return mat
def hill_climbing(mat,g):
  global q
  global visited
  visited=[]
  value_check=[]
  q=[]
  visited.append(mat)
  while(1):
    val1=heuristic(mat,g)
    new=move_left(mat)
    val2=heuristic(new,g)
    value_check.append([val2,new])
    new=move_right(mat)
    val3=heuristic(new,g)
    value_check.append([val3,new])
    new=move_up(mat)
    val4=heuristic(new,g)
    value_check.append([val4,new])
    new=move_down(mat)
    val5=heuristic(new,g)
    value_check.append([val5,new])
    elem=[[0,0,0],[0,0,0],[0,0,0]]
    value=0
    for each in value_check:
      if each[0]<val1:
        elem=each[1]
        value=each[0]
        break
    for each in value_check:
      value_check.remove(each)
    if(elem==g):
      print('found')
      print(elem)
      return
    else:
      if elem not in visited:
        q.append((elem,value))
        print(elem)
    if(len(q)>0):
      t=deque()
      mat=t[0]
      q=t[1]
      if mat not in visited:
        visited.append(mat)
    else:
      print('not found')
s=[[2,0,3],[1,8,4],[7,6,5]]
g=[[1,2,3],[8,0,4],[7,6,5]]
hill_climbing(s,g)

#Steepest Hill climbing:
import copy
def empty_tile(mat):
  for i in range(3):
    for j in range(3):
      if mat[i][j]==0:
        return([i,j])
def heuristic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d
def deque():
  global q
  new=[]
  for each in q:
    new.append(each[1])
  new.sort()
  for each in q:
    if(each[1]==new[0]):
      elem=each[0]
      print("elem",elem)
      break
  q.remove((elem,each[1]))
  return ((elem,q))
def move_up(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=0:
    mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_down(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=2:
    mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_left(mat):
  l=empty_tile(mat)
  i=l[0]
  j=l[1]
  mat1=copy.deepcopy(mat)
  if j!=0:
    mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
    return mat1
  else:
    return mat
def move_right(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if j!=2:
    mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
    return mat1
  else:
    return mat
def steepest_hill_climbing(mat,g):
  global q
  global visited
  visited=[]
  value_check=[]
  q=[]
  visited.append(mat)
  while(1):
    new=mat
    val1=heuristic(new,g)
    new=move_left(new)
    val2=heuristic(new,g)
    value_check.append([val2,new])
    new=move_right(mat)
    val3=heuristic(new,g)
    value_check.append([val3,new])
    new=move_up(mat)
    val4=heuristic(new,g)
    value_check.append([val4,new])
    new=move_down(mat)
    val5=heuristic(new,g)
    value_check.append([val5,new])
    min_case=min(value_check)
    min_val=min_case[0]
    min_elem=min_case[1]
    for each in value_check:
      value_check.remove(each)
    if(min_elem==g):
      print('found')
      print(min_elem)
      return
    else:
      if min_elem not in visited:
        q.append((min_elem,min_val))
        print(min_elem)
    if(len(q)>0):
      t=deque()
      mat=t[0]
      q=t[1]
      if mat not in visited:
        visited.append(mat)
    else:
      print('not found')
s=[[2,0,3],[1,8,4],[7,6,5]]
g=[[1,2,3],[8,0,4],[7,6,5]]
steepest_hill_climbing(s,g)

#A*
def enqueue(s,val):
    q.append((val,s))
    return q
def heuristic_val(s,curr_state,g):
    heur_val = heuristic(s,curr_state) + heuristic(g,curr_state)
    return heur_val
def empty_tile(mat):
  for i in range(3):
    for j in range(3):
      if mat[i][j]==0:
        return([i,j])
def move_up(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=0:
    mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_down(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if i!=2:
    mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
    return mat1
  else:
    return mat
def move_left(mat):
  l=empty_tile(mat)
  i=l[0]
  j=l[1]
  mat1=copy.deepcopy(mat)
  if j!=0:
    mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
    return mat1
  else:
    return mat
def move_right(mat):
  l=empty_tile(mat)
  mat1=copy.deepcopy(mat)
  i=l[0]
  j=l[1]
  if j!=2:
    mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
    return mat1
  else:
    return mat
def deque():
  global q
  new=[]
  for each in q:
    new.append(each[1])
  new.sort()
  for each in q:
    if(each[1]==new[0]):
      elem=each[0]
      print("elem",elem)
      break
  q.remove((elem,each[1]))
  return ((elem,q))
def astar_search(s,g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return
    global visited
    global q
    visited=[]
    q=[]
    while(1):
        new = move_up(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        new = move_down(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        new = move_right(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        new = move_left(curr_state)
        if new != curr_state:
            if new == g:
              print("found")
              return
            else:
                if new not in visited:
                    q.append((new,heuristic_val(s,new,g)))

        if len(q) > 0:
            t = deque()
            curr_state=t[0]
            q=t[1]
        else:
            print ("not found")
            return
import copy
s = [[2,0,3],[1,8,4],[7,6,5]]
g = [[1,2,3],[8,0,4],[7,6,5]]
global q
q=[]
global visited
visited=[]
visited = visited + [s]
astar_search(s,g)

#AO*
def Cost(H, condition, weight = 1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node]+weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B =' OR '.join(OR_nodes)
        PathB = min(H[node]+weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost

def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()
    least_cost= {}
    for key in Main_nodes:
        condition = Conditions[key]
        c = Cost(H, condition, weight)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, condition, weight)
    return least_cost

def shortest_path(Start,Updated_cost, H):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)

        Next = key[Index].split()
        if len(Next) == 1:
            Start =Next[0]
            Path += '<--' +shortest_path(Start, Updated_cost, H)
        else:
            Path +='<--('+key[Index]+') '
            Start = Next[0]
            Path += '[' +shortest_path(Start, Updated_cost, H) + ' + '
            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, H) + ']'
    return Path

H = {'A': 0, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}

Conditions = {
    'A': {'OR': ['D'], 'AND': ['B', 'C']},
    'B': {'OR': ['G', 'H']},
    'D': {'AND': ['E', 'F']},
}

weight = 1
print('Updated Cost :')
Updated_cost = update_cost(H, Conditions, weight=1)
print('*'*75)
print('Shortest Path :\n',shortest_path('A', Updated_cost,H))





