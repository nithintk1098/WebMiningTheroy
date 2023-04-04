import networkx as nx


d = 0.85


G = nx.DiGraph()
G.add_edge('B', 'A')
G.add_edge('C', 'A')
G.add_edge('C', 'B')
G.add_edge('D', 'B')
G.add_edge('C', 'D')


pagerank = nx.pagerank(G, alpha=d)


for page in pagerank:
    print(f"{page}: {pagerank[page]}")

sorted_pagerank = sorted(pagerank, key=lambda k: pagerank[k])

for page in sorted_pagerank[::-1]:
    print(page+"->",end="")
print("END")
