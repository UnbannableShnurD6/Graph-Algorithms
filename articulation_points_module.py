from route_search_module import route_search

def made_graph_copy_without_point(graph: dict, point: str):
    graph_copy = {}
    for point_it in graph:
        if point_it == point:
            continue
        graph_copy[point_it] = list(graph[point_it])
        if point in graph_copy[point_it]:
            graph_copy[point_it].remove(point)
    return graph_copy

# Тут ищутся точнки сочленения графов.
# Работает только для неореинтированных графов :(
def articulation_points(graph: dict):
    res = []

    for point in graph.keys():
        # Если точка является точкой сочленения - должна была нарушиться связность у точек сочленения
        graph_copy = made_graph_copy_without_point(graph, point)
        for i in graph[point]:
            for j in graph[point]:
                if point in res:
                    continue
                if (route_search(graph_copy, i, j) is None) != (route_search(graph, i, j) is None):
                    res.append(point)

    if len(res):
        print("Обнаружены точки сочленения:", res)
    else:
        print("Точек сочленения не обнаружено!")