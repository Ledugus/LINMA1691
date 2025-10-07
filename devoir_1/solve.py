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

    # number of nodes
    N = len(adj)

    # is a node already visited?
    visited = [False] * N
    # list of node to process in the second step
    L = []

    # queue of nodes to process with their associated status (i,False/True) i is the node index and True/False describes if we are appending the node to L or not when processing it
    q = deque()

    # Le but ici est de faire un tri topologique des noeuds -> DFS
    # On ajoute les noeuds à L une fois qu'on a fini d'explorer leurs descendants
    for x in range(N):
        if not visited[x]:
            q.append((x, False))

        while q:
            x, is_done_exploring = q.pop()

            if is_done_exploring:
                L.append(x)
                continue
            visited[x] = True
            q.append((x, True))
            for neightbour in adj_out[x]:
                if not visited[neightbour]:
                    q.append((neightbour, False))

    # Le premier à être traité est le dernier à être ajouté,
    # donc le dernier à avoir fini d'explorer -> il faut inverser L
    L.reverse()
    ans = 0

    visited = [False] * N

    # (Explication inspirée de https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/03/Small03.pdf)
    # On sait par la propriété du tri topologique que le dernier à être ajouté est forcément une racine d'une SCC
    # Et que cette SCC est forcément une source dans le DAG des SCCs
    # C'est donc une SCC optimale pour initier la rumeur
    # On explore tous ses descendants (peut contenir plusieurs SCCs)
    # Le prochain noeud non visité dans L est forcément la racine d'une autre SCC
    # source dans le DAG des SCC
    # En itérant de cette manière sur toutes les sources, on trouve le nombre
    # minimum de noeuds nécessaires pour atteindre tous les noeuds
    for node in L:
        if visited[node]:
            continue

        ans += 1
        visited[node] = True

        q = deque()
        q.append(node)
        while q:
            x = q.pop()
            visited[x] = True
            for adj in adj_out[x]:
                if not visited[adj]:
                    q.append(adj)

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
