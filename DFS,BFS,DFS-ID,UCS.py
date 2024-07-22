#DFS
import copy
#s=[['A'],['C','B'],[]]
s=[['A','B'],['C'],[]]
g=['C','B','A']
open=[]
closed=[]
def generate_children(s):
  l=[]
  for i in range(len(s)):
    if(len(s[i])!=0):
      for j in range(len(s)):
        s1=copy.deepcopy(s)
        if(j!=i):
          x=s1[i][0]
          s1[i].remove(x)
          s1[j].insert(0,x)
          l.append(s1)
  return l
def dfs_search(s1,g):
  open=[]
  closed=[]
  while(1):
      s=copy.deepcopy(s1)
      l = generate_children(s)
      for each in l:
        if each not in open and each not in closed:
          open.append(each)
      if len(open) > 0:
        s1 = open[len(open)-1]
        del(open[len(open)-1])
        print(s1)
        closed.append(s1)
        for each in s1:
          if each==g:
            print("found")
            return
      else:
        print ("not found")
dfs_search(s,g)

#BREADTH FIRST SEARCH
import copy
#s=[['A'],['C','B'],[]]
s=[['A','B'],['C'],[]]
g=['C','B','A']
open=[]
closed=[]
def generate_children(s):
  l=[]
  for i in range(len(s)):
    if(len(s[i])!=0):
      for j in range(len(s)):
        s1=copy.deepcopy(s)
        if(j!=i):
          x=s1[i][0]
          s1[i].remove(x)
          s1[j].insert(0,x)
          l.append(s1)
  return l
def bfs_search(s1,g):
  open=[]
  closed=[]
  while(1):
      s=copy.deepcopy(s1)
      l = generate_children(s)
      for each in l:
        if each not in open and each not in closed:
          open.append(each)
          print(open)
      if len(open) > 0:
        s1 = open[0]
        del(open[0])
        print(s1)
        closed.append(s1)
        for each in s1:
          if each==g:
            print("found")
            return
      else:
        print ("not found")
bfs_search(s,g)
#DLS:

#DFS-ID:
import copy
s=[['A','B'],['C'],[]]
g=['C','B','A']
open=[]
closed=[]
def generate_children(s):
  l=[]
  for i in range(len(s)):
    if(len(s[i])!=0):
      for j in range(len(s)):
        s1=copy.deepcopy(s)
        if(j!=i):
          x=s1[i][0]
          s1[i].remove(x)
          s1[j].insert(0,x)
          l.append(s1)
  return
def dfsid_search(s1,g):
  open=[[]]
  closed=[]
  i=0
  while(1):
      s=copy.deepcopy(s1)
      l = generate_children(s)
      i=i+1
      for each in l:
        if each not in open and each not in closed:
          open.append(each)
          print(open)
      open1=copy.deepcopy(open)
      closed1=[]
      while len(list(open1)) > 0:
        s1 = list(open1)[len(list(open1))-1]
        del(open1[len(list(open1))-1])
        closed1.append(s1)
        print(s1)
        for each in s1:
          if each==g:
            print("found at depth ",i)
            return
      if len(list(open)) > 0:
        s1 = list(open)[len(list(open))-1]
        del(open[len(list(open))-1])
        closed.append(s1)
      else:
        print ("not found")
dfsid_search(s,g)

#UCS:
def uniform_cost_search(goal, start):
  global graph
  queue = []
  answer=1000000 #optimal path cost
  queue.append([0, start])
  visited = {}
  while (len(queue) > 0):
    queue = sorted(queue)
    print(queue)
    p = queue[0]
    del queue[0]
    if(p[1]==goal):
      if (answer > p[0]):
        answer = p[0]
        del queue[0]
        return answer
    if (p[1] not in visited):
      for i in range(len(graph[p[1]])):
        if(graph[p[1]][i]!=0):
          queue.append( [(p[0] + graph[p[1]][i]), i])
          visited[p[1]] = 1
  return answer


graph=[[0,2,0,5,0,0,0],[2,0,4,5,0,0,1],[0,4,0,0,4,6,0],[5,5,0,2,0,0,6],[0,0,4,2,0,3,7],[0,0,6,0,3,0,3],[0,1,0,6,7,3,0]]
goal = 6
answer = uniform_cost_search(goal, 0)
print("Minimum cost from 0 to 6 is = ",answer)




