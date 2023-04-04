import numpy as np

d = 0.85
pages = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['C']
}
pagerank = {}
N = len(pages)

for page in pages:
    pagerank[page] = 1.0

def calculate_pagerank(pages, pagerank, d, N):
    new_pagerank = {}
    for page in pages:
        incoming_links = [p for p in pages if page in pages[p]]
        score = 0.0
        for link in incoming_links:
            score += pagerank[link] / len(pages[link])
        new_pagerank[page] = (1 - d) + d * score
    for page in pages:
        pagerank[page] = new_pagerank[page]

iterations = 10
for i in range(iterations):
    calculate_pagerank(pages, pagerank, d, N)

for page in pagerank:
    print(f"{page}: {pagerank[page]}")

sorted_pagerank = sorted(pagerank, key=lambda k: pagerank[k])

for page in sorted_pagerank[::-1]:
    print(page+"->",end="")
print("END")
