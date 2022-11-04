'''
Author: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
Date: 2022-11-04 15:20:42
LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
LastEditTime: 2022-11-04 16:46:00
FilePath: \algrithm_design-1\project3\problem3s2.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from networkx.algorithms import isomorphism
import networkx as nx
import matplotlib.pyplot as plt

def could_be_isomorphic(G1, G2):
    """Returns False if graphs are definitely not isomorphic.
    True does NOT guarantee isomorphism.

    Parameters
    ----------
    G1, G2 : graphs
       The two graphs G1 and G2 must be the same type.

    Notes
    -----
    Checks for matching degree, triangle, and number of cliques sequences.
    """

    # Check global properties
    if G1.order() != G2.order():
        return False

    # Check local properties
    d1 = G1.degree()
    t1 = nx.triangles(G1)
    c1 = nx.number_of_cliques(G1)
    props1 = [[d, t1[v], c1[v]] for v, d in d1]
    props1.sort()

    d2 = G2.degree()
    t2 = nx.triangles(G2)
    c2 = nx.number_of_cliques(G2)
    props2 = [[d, t2[v], c2[v]] for v, d in d2]
    props2.sort()

    if props1 != props2:
        return False

    # OK...
    return True


graph_could_be_isomorphic = could_be_isomorphic


def fast_could_be_isomorphic(G1, G2):
    """Returns False if graphs are definitely not isomorphic.

    True does NOT guarantee isomorphism.

    Parameters
    ----------
    G1, G2 : graphs
       The two graphs G1 and G2 must be the same type.

    Notes
    -----
    Checks for matching degree and triangle sequences.
    """
    # Check global properties
    if G1.order() != G2.order():
        return False

    # Check local properties
    d1 = G1.degree()
    t1 = nx.triangles(G1)
    props1 = [[d, t1[v]] for v, d in d1]
    props1.sort()

    d2 = G2.degree()
    t2 = nx.triangles(G2)
    props2 = [[d, t2[v]] for v, d in d2]
    props2.sort()

    if props1 != props2:
        return False

    # OK...
    return True


fast_graph_could_be_isomorphic = fast_could_be_isomorphic


def faster_could_be_isomorphic(G1, G2):
    """Returns False if graphs are definitely not isomorphic.

    True does NOT guarantee isomorphism.

    Parameters
    ----------
    G1, G2 : graphs
       The two graphs G1 and G2 must be the same type.

    Notes
    -----
    Checks for matching degree sequences.
    """
    # Check global properties
    if G1.order() != G2.order():
        return False

    # Check local properties
    d1 = sorted(d for n, d in G1.degree())
    d2 = sorted(d for n, d in G2.degree())

    if d1 != d2:
        return False

    # OK...
    return True


faster_graph_could_be_isomorphic = faster_could_be_isomorphic


if __name__ == "__main__":
    G1 = nx.Graph()
    G1.add_nodes_from([1, 2, 3, 4, 5])
    G1.add_edges_from([(1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)])
    G2 = nx.Graph()
    G2.add_nodes_from([1, 2, 3, 4, 5])
    G2.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 4), (3, 4), (3, 5), (4, 5)])
    GM = isomorphism.GraphMatcher(G1, G2)
    print("TestCase1: " + str(GM.is_isomorphic()))

    G3 = nx.Graph()
    G4 = nx.Graph()
    G3.add_nodes_from([1, 2, 3, 4, 5, 6])
    G4.add_nodes_from([1, 2, 3, 4, 5, 6])
    G3.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 3), (2, 6), (3, 4), (4, 5), (4, 6), (5, 6)])
    G4.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 5), (4, 6), (5, 6)])
    GM = isomorphism.GraphMatcher(G3, G4)
    print("TestCase2: " + str(GM.is_isomorphic()))

    G5 = nx.Graph()
    G6 = nx.Graph()
    G5.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    G6.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    G5.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (3, 6), (4, 7), (5, 6), (5, 7), (6, 7)])
    G6.add_edges_from([(1, 2), (1, 4), (1, 6), (2, 3), (2, 5), (3, 4), (3, 6), (4, 6), (4, 7), (5, 7), (6, 7)])
    GM = isomorphism.GraphMatcher(G5, G6)
    print("TestCase3: " + str(GM.is_isomorphic()))