#8 PUZZLE:
q=[]
visited=[] #global variable
def comp(s, g):
    if s==g:
      return 1
    else:
      return 0 
#finding pos of zero so that swapping cane be done
def  find_pos(s): 
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i][j]==0:
                    return[i,j]         
#modified up,  new is making copy of s, any changes made in new will not be reflected in s
def up1(s):
    pos=find_pos(s)
    #print(pos)
    row=pos[0]
    clm=pos[1]
    new=copy.deepcopy(s)
    if row>0: #we cannot move up if there is no row.
        new[row][clm]=new[row-1][clm]
        new[row-1][clm]=0
        print("new state is", new)
    return new
def down(s):
    pos=find_pos(s)
    row=pos[0]
    clm=pos[1]
    new=copy.deepcopy(s)
    if row<2: #cannot move down here is no row in bottom
        new[row][clm]=new[row+1][clm]
        new[row+1][clm]=0
        print("new state is", new)
    return new
def left(s):
    pos=find_pos(s)
    row=pos[0]
    clm=pos[1]
    new=copy.deepcopy(s)
    if clm>0:
        new[row][clm]=new[row][clm-1]
        new[row][clm-1]=0
        print("new state is" ,new)
    return new
def right(s):
    pos=find_pos(s)
    row=pos[0]
    clm=pos[1]
    new=copy.deepcopy(s)
    if clm<2:
        new[row][clm]=new[row][clm+1]
        new[row][clm+1]=0
        print("new state is", new)
    return new
def gen_chil(s):
    global q
    global visited
    new_state=up1(s)
    if new_state not in q and new_state not in visited:
         q.append(new_state)
    new_state=down(s)
    if new_state not in q and new_state not in visited:
         q.append(new_state)
    new_state=left(s)        
    if new_state not in q and new_state not in visited:
         q.append(new_state)
    new_state=right(s)        
    if new_state not in q and new_state not in visited:
         q.append(new_state)
        
#initial state will be checked present in q,remove s0,if s0== g:found, if not children of s0 will be genrated:s1,s2,s3,s4
#same thing will be done with s1,its children will be appended in the ned of q but added state should not be already present
#in q and it should have not been visited before(compared with goal and children generated)
def search(g):
    global q
    global visited
    print(q)
    while(1):
        s=q[0]
        del q[0]
        if comp(s, g)==1:
            print("found")
            return
        else:   #if state is not found, children will be generated u, d ,l  and r
            gen_child(s)
            visited.append(s)
    print("-------")
    print(q)   
s=[[1,2,3],[8,0,4],[7,6,5]] #start
g=[[2,8,1],[0,4,3],[7,6,5]] #goal
q.append(s)
search(g) 
print(len(visited))

#WATER JUG
from collections import defaultdict
#default dic: recursively will call the function
#transfer from j2 to j1 untilj2 is empty or j1 is full
j1=int(input("enter first jug value"))
j2=int(input("enter second jug value"))
target=int(input("enter final jug value"))
visited=defaultdict(lambda:False) #key having value as false
print(visited)
def waterjug(amt1,amt2):
    #amt1 and amt2 are 2 capacities of jugs
    if(amt1==target and amt2==0) or (amt1==0 and amt2==target):
        print("amt1",amt1," ","amt2",amt2)
        #print("amt2",amt2)
        return True
    if visited[(amt1,amt2)]==False:
        print("amt1",amt1," ","amt2",amt2)
        visited[(amt1,amt2)]=True  #now node is visited, set it to true so that not visited again
        return(waterjug(0,amt2) or
               waterjug(amt1,0) or
               waterjug(j1,amt2) or
               waterjug(amt1,j2)or
               waterjug(amt1+min(amt2,(j1-amt1)),amt2-min(amt2,(j1-amt1))) or
               waterjug(amt1-min(amt1,(j2-amt2)),amt2+min(amt1,(j2-amt2))))
    else:
        return False                                                                                                                                 
print("step")  
waterjug(0,0) #start from 0,0,function called, check if condition is true,  if true print amt1 and amt2 else go to visited and set true, now call recursively

#TSP: 
from sys import maxsize 
from itertools import permutations
V = 4
def TSP(graph, s): 

	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:
		current_pathweight = 0
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 
if __name__ == "__main__": 
	graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
			[15, 35, 0, 30], [20, 25, 30, 0]] 
	s = 0
	print(TSP(graph, s))





