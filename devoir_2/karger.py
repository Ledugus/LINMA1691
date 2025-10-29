"""
Student template for the second homework of LINMA1691: "Théorie des graphes".
"""

import math
import random


class Union_Find:
    """
    Disjoint sets data structure for Kruskal's or Karger's algorithm.

    It is useful to keep track of connected components (find(a) == find(b) iff they are connected).

    """

    def __init__(this, N):
        """
        Corresponds to MakeSet for all the nodes
        INPUT :
            - N : the initial number of disjoints sets
        """
        this.N = N
        this.p = list(range(N))
        this.size = [1] * N

    def union(this, a, b):
        """
        INPUT :
            - a and b : two elements such that 0 <= a, b <= N-1
        OUTPUT:
            - return nothing

        After the operation, the two given sets are merged
        """
        a = this.find(a)
        b = this.find(b)

        if a == b:
            return

        # Swap variables if necessary
        if this.size[a] > this.size[b]:
            a, b = b, a

        this.size[b] += this.size[a]
        this.p[a] = b

    def find(this, a):
        """
        INPUT :
            - a : one element such that 0 <= a <= N-1
        OUTPUT:
            - return the root of the element a
        """
        if a != this.p[a]:
            this.p[a] = this.find(this.p[a])
        return this.p[a]


def min_cut(N, edges):
    """
    INPUT :
        - N the number of nodes
        - edges, list of tuples (u, v) giving an edge between u and v

    OUTPUT :
        - return an estimation of the min cut of the graph

    This method has to return the correct answer with probability bigger than 0.999
    See project homework for more details
    """

    def karger(nodes, edges):
        """
        INPUT :
            - N the number of nodes
            - edges, list of tuples (u, v) giving an edge between u and v

        OUTPUT :
            - return an estimation of the min cut of the graph

        See project homework for more details
        """

        this_min_cut = -1

        # TO COMPLETE

        return this_min_cut

    best_min_cut = -1

    p = N * (N - 1) / 2
    p_value = 0.999
    k = math.ceil(math.log((1 - p_value)) / math.log(1 - 1 / p))
    print(k)
    for i in range(k):
        this_min_cut = karger(N, edges)
        if best_min_cut == -1 or this_min_cut < best_min_cut:
            best_min_cut = this_min_cut

    return best_min_cut


if __name__ == "__main__":

    # Read Input for the second exercice

    with open("in2.txt", "r") as fd:
        l = fd.readline()
        l = l.rstrip().split(" ")

        n, m = int(l[0]), int(l[1])

        edges = []
        for edge in range(m):

            l = fd.readline().rstrip().split()
            edges.append(tuple([int(x) for x in l]))

    # Compute answer for the second exercice

    ans = min_cut(n, edges)

    # Check results for the second exercice

    with open("out2.txt", "r") as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output))
