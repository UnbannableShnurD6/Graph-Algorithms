from route_search_module import route_search

# Тут проверяется связность графов
# Пока работает только с неореинтированными графами
def graph_connectivity(graph: dict):
    for i in graph.keys():
        for j in graph.keys():
            if route_search(graph, i, j) is None:
                print("Граф не является связным: нет пути от " + i + " до " + j)
                return

    print("Граф является связным!")