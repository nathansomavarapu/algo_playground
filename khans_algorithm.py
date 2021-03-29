import random
import networkx as nx
import matplotlib.pyplot as plt 

### Graph is given as an adjacency list
### G = [(U,V), ..., ]
### Nodes: 0 < i < n-1

def generate_random_graph(n):
    edge_list = []
    for i in range(n):
        for j in range(i+1,n):
            if random.random() > 0.3:
                edge_list.append((i, j))
    
    return edge_list

def vizualize(n, edge_list):
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edge_list)

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png") 

def khans_algorithm(n, edge_list):
    
    outgoing_dict = {}
    incoming_dict = {}
    empty_inc = set()
    topo = []

    for i in range(n):
        outgoing_dict[i] = set()
        incoming_dict[i] = set()

    for e in edge_list:
        u,v = e
        outgoing_dict[u].add(v)
        incoming_dict[v].add(u)

    for k in incoming_dict.keys():
        if len(incoming_dict[k]) == 0:
            empty_inc.add(k)

    while len(empty_inc) != 0:
        curr = empty_inc.pop()
        update_list = outgoing_dict[curr]
        for node in update_list:
            incoming_dict[node].remove(curr)
            if len(incoming_dict[node]) == 0:
                empty_inc.add(node)

        del incoming_dict[curr] 
        topo.append(curr)
    
    if len(incoming_dict) != 0:
        print("Error: The graph is not a DAG!")
        exit()

    return topo

def main():
    n = 5
    edge_list = generate_random_graph(n)

    vizualize(n, edge_list)

    topo = khans_algorithm(n, edge_list)
    print(topo)

if __name__ == "__main__":
    main()