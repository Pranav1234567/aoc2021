import time
def construct_graph(graph, s, e):
    if s not in graph:
        graph[s] = set()
    if e not in graph:
        graph[e] = set()

    graph[s].add(e)
    graph[e].add(s)

def construct_paths(graph):
    queue = [['start']]
    final_paths = []
    start_time = time.time()

    while queue != []:
        path = queue[0]
        queue = queue[1:]
        if path[-1] != 'end':
            queue.extend([path + [c] for c in graph[path[-1]] if (c != 'start' and (c.isupper() or (c.islower() and c not in set(path))))])
        else:
            final_paths.append(path)
    print("--- %s seconds ---" % (time.time() - start_time))

    print(len(final_paths))

start_time = time.time()
with open('day12_input.txt') as f:
    lines = f.readlines()
    graph = dict()
    for line in lines:
        s, e = line.rstrip().split('-')
        construct_graph(graph, s, e)
    construct_paths(graph)
