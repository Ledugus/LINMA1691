from collections import deque


"""
    Solves the problem defined in the statement for adj an adjacency list of the dispersion dynamics of rumors in LLN
        adj is a list of length equal to the number of kots
        adj[i] gives a list of kots touched by i with direct edges (0-based indexing)

    You are free to change the code below and to not use the precompleted part. The code is based on the high-level description at https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
    You can also define other sub-functions or import other datastructures from the collections library
"""


def solve(adj):
    # adjacency of the graph and its transpose
    adj_out = adj
    
    adj_in = transpose(adj_out)
    # number of nodes
    N = len(adj_in)

    # is a node already visited?
    visited = [False]*N
    # list of node to process in the second step
    L = []
   
    # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it
    q = deque()

    ### loop on every node and launch a visit of its descendants
    ### On va faire une boucle sur tous les noeuds
     
    for x in range(N):
        if(visited[x] == False):
            q.append((x,False))
    
        
        
        while q:
            x,to_append = q.pop()


            if to_append:
                L.append(x)
            else : 
                visited[x] = True
                q.append((x, True))    
                for neightboor in adj_in[x]: 
                    if(visited[neightboor] == False):
                        q.append((neightboor , False))

                              
                    
                
    ### reverse the list to obtain the post-order  
    
    L.reverse()
    ans = 0

    visited = [False]*N
    
    
    
    
    
    for component in L: 

        if(visited[component] == False):
            queu = deque()
            queu.append(component)
            visited[component] = True
            ans += 1
            while queu: 
                x = queu.pop()
                visited[x] = True

                for neight_boor in adj_out[x]: 
                    if(visited[neight_boor] == False):
                        queu.append(neight_boor)
            

    


    return ans


"""
    Transpose the adjacency matrix
        Construct a new adjacency matrix by inverting all the edges: (x->y) becomes (y->x) 
"""


def transpose(adj):
    adj_in = [list() for _ in range(len(adj))]

    n = len(adj)

    for i in range(n):
        for node in adj[i]:
            adj_in[node].append(i)

    return adj_in
