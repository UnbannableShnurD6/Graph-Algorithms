from route_search_module import route_search

# Тут ищутся мосты графов
def brige_search(graph: dict):
    briges = []

    for i in graph.keys():
        for j in graph[i]:
            graph_copy = dict(graph)
            graph_copy[i] = list(graph[i])
            graph_copy[i].remove(j)
            if route_search(graph_copy, i, j) is None:
                briges.append(f"{i}->{j}")

    if len(briges):
        print("Обнаружены мосты:", briges)
    else:
        print("Мостов не обнаружено!")