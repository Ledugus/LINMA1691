import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""


def eulerian_path_finder(graph):
    eulerian_path = []

    adj = copy.deepcopy(graph)

    noeud_impair = [i for i in range(len(adj)) if len(adj[i]) % 2 == 1]
    if len(noeud_impair) > 2:
        return None
    u = 0
    v = 0
    if len(noeud_impair) == 2:
        u, v = noeud_impair
        adj[u].append(v)
        adj[v].append(u)

    # début de l'algo
    stack = []
    current = 0
    # tant que des arêtes restent à explorer
    while stack or adj[current]:
        if not adj[current]:
            eulerian_path.append(current)
            current = stack.pop()

        else:
            stack.append(current)
            next = adj[current].pop()
            adj[next].remove(current)
            current = next

    # ajouter le dernier noeud
    eulerian_path.append(current)
    # fin de l'algo

    # adapter la solution si arête ajoutée
    if len(noeud_impair) == 2:
        for i in range(len(eulerian_path) - 1):
            if (eulerian_path[i] == u and eulerian_path[i + 1] == v) or (
                eulerian_path[i] == v and eulerian_path[i + 1] == u
            ):
                # concatener la fin du chemin avec le début, ce qui coupe l'arête ajoutée
                # on prend pas le premier élément du début parce qu'il est déjà à la fin (cycle)
                eulerian_path = eulerian_path[i + 1 :] + eulerian_path[1 : i + 1]
                break

    return eulerian_path
