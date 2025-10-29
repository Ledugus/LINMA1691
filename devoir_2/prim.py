"""
Student template for the second homework of LINMA1691: "Théorie des graphes".
"""

import math
import heapq


def prim_mst(N, roads):
    """
    INPUT :
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved

        See homework statement for more details
    """

    total_satisfaction = 0

    # Construire la liste d'adjacence
    adj = [set() for i in range(N)]
    for u, v, s in roads:
        total_satisfaction += s
        adj[u].add((v, s))
        adj[v].add((u, s))

    # Initialiser la file de priorité
    roads_to_visit = []
    heapq.heapify(roads_to_visit)

    # Choisir un noeud arbitraire pour lancer
    first_node = roads[0][0]
    visited = set([first_node])
    # Ajouter les arêtes adjacentes au premier noeud
    for v, s in adj[first_node]:
        heapq.heappush(roads_to_visit, (s, v))

    # Tant qu'on n'a pas un arbre couvrant
    while len(visited) < N:
        # choisir la meilleure arête de la heap
        s, node_to_add = heapq.heappop(roads_to_visit)
        # sauf si elle est déjà dans l'arbre
        if node_to_add in visited:
            continue
        total_satisfaction -= s
        visited.add(node_to_add)
        # ajouter les arêtes adjacentes au noeud ajouté
        for neighbour, s2 in adj[node_to_add]:
            if neighbour not in visited:
                heapq.heappush(roads_to_visit, (s2, neighbour))

    return total_satisfaction


if __name__ == "__main__":

    # Read Input for the first exercice

    with open("in1.txt", "r") as fd:
        l = fd.readline()
        l = l.rstrip().split(" ")

        n, m = int(l[0]), int(l[1])

        roads = []
        for road in range(m):

            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))

    # Compute answer for the first exercice

    ans1 = prim_mst(n, roads)

    # Check results for the first exercice

    with open("out1.txt", "r") as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output))
