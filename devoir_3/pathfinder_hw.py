def eulerian_path_finder(graph):
    n = len(graph)
    # degrés impairs
    noeud_impair = [i for i, nbrs in enumerate(graph) if len(nbrs) % 2 == 1]
    if len(noeud_impair) > 2:
        return None

    # Construction efficace des arêtes (une arête non orientée -> un id)
    adj = [[] for _ in range(n)]  # listes de (voisin, edge_id)
    eid = 0
    for u, nbrs in enumerate(graph):
        for v in nbrs:
            if u <= v:  # n'ajoute l'arête qu'une seule fois pour la paire (u,v)
                adj[u].append((v, eid))
                adj[v].append((u, eid))
                eid += 1

    # si deux noeuds impairs, ajoute une arête artificielle pour former un cycle
    added_pair = None
    if len(noeud_impair) == 2:
        u, v = noeud_impair
        adj[u].append((v, eid))
        adj[v].append((u, eid))
        added_pair = (u, v)
        eid += 1

    # tableau de marquage des arêtes visitées (bytearray plus compact)
    visited = bytearray(eid)

    # choix du noeud de départ
    start = (
        noeud_impair[0]
        if noeud_impair
        else next((i for i, nbrs in enumerate(adj) if nbrs), 0)
    )

    stack = []
    current = start
    eulerian_path = []
    while stack or adj[current]:
        while adj[current]:
            v, e = adj[current].pop()
            if visited[e]:
                continue
            visited[e] = 1
            stack.append(current)
            current = v
            break
        else:
            eulerian_path.append(current)
            if not stack:
                break
            current = stack.pop()
    eulerian_path.append(current)

    # si on avait ajouté une arête artificielle, on la coupe pour obtenir le chemin
    if added_pair is not None:
        u, v = added_pair
        for i in range(len(eulerian_path) - 1):
            a, b = eulerian_path[i], eulerian_path[i + 1]
            if (a == u and b == v) or (a == v and b == u):
                eulerian_path = eulerian_path[i + 1 :] + eulerian_path[1 : i + 1]
                break

    return eulerian_path
