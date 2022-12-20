# [markdown]
# preprocessing data loop to find all the shortest path from starting point to all remain value-exist node (candidate node)
# in the graph next we pass this list of all shortest path to the function which is - ensure this path can be archive
# under the remaining moves the total pressure this path can release, so, the case with we never pick any node is
# included, choose the biggest one. Now the starting node will be moved to this node. loop this process again and
# again util, out of move or when the pressure the case which we not pick anything is the biggest . Note that
# everytime we pick the next node, all candidate node must be excluded the previous pick

#%%
data = open('input/day16_small.txt').read().splitlines()
data = [line.replace("Valve ", "")
 .replace(" has flow rate=", " ")
 .replace("; tunnels lead to valves ", " ")
    .replace("; tunnel leads to valve ", " ")
 .replace(", "," ") for line in data]
data = [line.split() for line in data]
data = [[line[0], int(line[1]), line[2:]] for line in data]
#%%
import networkx
G = networkx.DiGraph()
for line in data:
    G.add_node(line[0])
    for node in line[2]:
        G.add_edge(line[0], node)
#%% Plot the graph G
import matplotlib.pyplot as plt
pos = networkx.spring_layout(G)
networkx.draw(G, pos, with_labels=True)
plt.show()


#%%
# from timeit import default_timer as timer
# start = timer()
remaining_node_with_flow = {node[0]:node[1] for node in data}
remaining_mins = 30
current_pressure = 0
current_pressure_per_min = 0
real_track = ['AA']
next_candidate = 'AA'
predict_pressure_track_for_each_candidate = {}
all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='AA', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure_per_min * (30 - mock_remaining_mins) + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure

remaining_mins = 27
current_pressure += 21 * 3
current_pressure_per_min += remaining_node_with_flow['JJ']
real_track.append('JJ')
remaining_node_with_flow.pop('JJ')
next_candidate = 'JJ'

#%%
predict_pressure_track_for_each_candidate = {}
all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='JJ', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    # print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    # print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure_per_min * (30 - mock_remaining_mins) + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    # print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure


remaining_mins = 24
current_pressure += (21 + 20) * 3
current_pressure_per_min += remaining_node_with_flow['DD']
real_track.append('DD')
remaining_node_with_flow.pop('DD')
next_candidate = 'DD'
#%%
predict_pressure_track_for_each_candidate = {}
all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='DD', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    # print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    # print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure_per_min * (30 - mock_remaining_mins) + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    # print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure



remaining_mins = 20
current_pressure += (21 + 20 + 22) * 4
current_pressure_per_min += remaining_node_with_flow['HH']
real_track.append('HH')
remaining_node_with_flow.pop('HH')
next_candidate = 'HH'
#%%

predict_pressure_track_for_each_candidate = {}
all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='HH', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    # print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    # print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure_per_min * (30 - mock_remaining_mins) + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    # print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure
#%%
remaining_mins = 14
current_pressure += (21 + 20 + 22 + 13) * 6
current_pressure_per_min += remaining_node_with_flow['BB']
real_track.append('BB')
remaining_node_with_flow.pop('BB')
next_candidate = 'BB'

#%%
all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='DD', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    if mock_remaining_mins < 0:
        continue
    print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure * 30 + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure


remaining_mins = 20
current_pressure += remaining_node_with_flow['HH']
real_track.append('HH')
remaining_node_with_flow.pop('HH')
next_candidate = 'HH'
#%%

all_shortest_paths = []
for node in remaining_node_with_flow.keys():
    all_shortest_paths.append(networkx.shortest_path(G, source='HH', target=node))
for node,flow in remaining_node_with_flow.items():
    if flow == 0:
        all_shortest_paths = [path for path in all_shortest_paths if path[-1] != node]
for path in all_shortest_paths:
    print(f"candidate is {path[-1]}")
    mock_remaining_mins = remaining_mins - (len(path) - 1) - 1
    if mock_remaining_mins < 0:
        continue
    print(f"remaining mins is {mock_remaining_mins}")
    predict_pressure = current_pressure * 30 + remaining_node_with_flow[path[-1]] * mock_remaining_mins
    print(f"predict pressure is {predict_pressure}")
    predict_pressure_track_for_each_candidate[path[-1]] = predict_pressure


#%%
# def find_next_best_node(current_node):
#     for node in candidate_node_dict.keys():
#         all_shortest_path = networkx.shortest_path(G, source=current_node, target=node)
#     for path in all_shortest_path:
#         max_pressure_can_reach = current_pressure
#         if len(path) == 1:
#%%




