data = open('input/day12.txt').read().split()
# %%
import matplotlib.pyplot as plt
import networkx as nx
from pyvis.network import Network
# %%
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)
        self.add_node(from_node)
        self.add_node(to_node)

    def find_all_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.edges:
            return []
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.find_all_path(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def bfs_to_find_path(self, start, end):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.edges[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def visualize(self):
        nx_G = nx.Graph()
        nx_G.add_nodes_from(self.nodes)
        for node, edges in self.edges.items():
            for edge in edges:
                nx_G.add_edge(node, edge)
        nx.draw(nx_G,node_size=1)
        plt.show()
    def visualize_in_html(self):
        nx_G = nx.Graph()
        nx_G.add_nodes_from(self.nodes)
        for node, edges in self.edges.items():
            for edge in edges:
                nx_G.add_edge(node, edge)
        nx.draw(nx_G,node_size=1)
        nt = Network()
        nt.from_nx(nx_G)
        nt.show("nx.html")
    def shortest_path(self, start, end):
        nx_G = nx.Graph()
        nx_G.add_nodes_from(self.nodes)
        for node, edges in self.edges.items():
            for edge in edges:
                nx_G.add_edge(node, edge)
        return nx.shortest_path(nx_G, start, end)



# %%
G = nx.DiGraph()

for row_i, row in enumerate(data):
    for col_i, col in enumerate(row):
        # find all up,down,left,right base on position
        current = data[row_i][col_i]
        up = data[row_i - 1][col_i]  if row_i - 1 >= 0 else '#'
        down = data[row_i + 1][col_i] if row_i + 1 < len(data) else '#'
        left = data[row_i][col_i - 1] if col_i - 1 >= 0 else '#'
        right = data[row_i][col_i + 1] if col_i + 1 < len(data[0]) else '#'
        # print(current, up, down, left, right)
        if current == 'S':
            if up in ['a', 'b']:
                G.add_edge(f'{row_i},{col_i}', f'{row_i - 1},{col_i}')
            if down in ['a', 'b']:
                G.add_edge(f'{row_i},{col_i}', f'{row_i + 1},{col_i}')
            if left in ['a', 'b']:
                G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i - 1}")
            if right in ['a', 'b']:
                G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i + 1}")
        if current == 'E':
            if up in ['y', 'z']:
                G.add_edge(f"{row_i - 1},{col_i}", f"{row_i},{col_i}")
            if down in ['y', 'z']:
                G.add_edge(f"{row_i + 1},{col_i}", f"{row_i},{col_i}")
            if left in ['y', 'z']:
                G.add_edge(f"{row_i},{col_i - 1}", f"{row_i},{col_i}")
            if right in ['y', 'z']:
                G.add_edge(f"{row_i},{col_i + 1}", f"{row_i},{col_i}")

        if (ord(up) - ord(current) in [0, 1]) or ( ord(up) < ord(current) and up != 'E' ):
            G.add_edge(f"{row_i},{col_i}", f"{row_i - 1},{col_i}")
        if ( ord(down) - ord(current) in [0, 1] ) or ord(down) < ord(current) and down != 'E':
            G.add_edge(f"{row_i},{col_i}", f"{row_i + 1},{col_i}")
        if ( ord(left) - ord(current) in [0, 1] ) or ord(left) < ord(current) and left != 'E':
            G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i - 1}")
        if ( ord(right) - ord(current) in [0, 1] ) or ord(right) < ord(current) and right != 'E':
            G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i + 1}")
        if current == 'a':
            if up == 'S':
                G.add_edge(f"{row_i - 1},{col_i}", f"{row_i},{col_i}")
            if down == 'S':
                G.add_edge(f"{row_i + 1},{col_i}", f"{row_i},{col_i}")
            if left == 'S':
                G.add_edge(f"{row_i},{col_i - 1}", f"{row_i},{col_i}")
            if right == 'S':
                G.add_edge(f"{row_i},{col_i + 1}", f"{row_i},{col_i}")
        if current in ['z', 'y']:
            if up == 'E':
                G.add_edge(f"{row_i},{col_i}", f"{row_i - 1},{col_i}")
            if down == 'E':
                G.add_edge(f"{row_i},{col_i}", f"{row_i + 1},{col_i}")
            if left == 'E':
                G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i - 1}")
            if right == 'E':
                G.add_edge(f"{row_i},{col_i}", f"{row_i},{col_i + 1}")
# %% find shorted path
# %%
# index of 'S' and 'E'
start, end = None, None
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            start = f'{i},{j}'
        if data[i][j] == 'E':
            end = f'{i},{j}'
#%%
a = nx.single_source_shortest_path(G, start)
#%%
shortest_path_can_find = nx.shortest_path(G, start, end)
#%%
for _, path in a.items():
    s,e = path[-1].split(',')
    if len(path) == 245:
        print(path[-1])
        shortest_path_can_find = path


# %%
all_a_location = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] in  ['a','S']:
            all_a_location.append(f'{i},{j}')
#%%
shortest_path_length_from_a_to_end = []
for location in all_a_location:
    try:
        l = nx.shortest_path_length(G, location, end)
        shortest_path_length_from_a_to_end.append(l)
    except:
        pass
#%%
min(shortest_path_length_from_a_to_end)
#%%


# %% Draw path
# %%
with open('/home/vermin/repo/aoc/output_day_12_2.txt', 'w') as f:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if f'{i},{j}' in shortest_path_can_find:
                f.write(data[i][j])
            else:
                f.write('#')
        f.write('\n')

#%%

import matplotlib.pyplot as pl

#%%
def draw_path(G, location):
    pl.clf()
    pl.plot(location[0], location[1], label=f'{location[0]} - {location[1]}')
    pl.plot(location[0], location[1], label=f'{location[0 ]}')

#%%
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] in  ['a','S']:
            draw_path(G, (i,j))
