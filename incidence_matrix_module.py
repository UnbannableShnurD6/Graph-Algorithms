# Тут строится матрица инцидентности.
def incidence_matrix(graph: dict):
    # Делаем копию графа, чтобы можно было из него какие-то вершины выкидывать
    graph_copy = graph

    # Сначала печатаем столбцы
    print("\t\t", end="")
    for point_name in graph.keys():
        print(point_name + "\t", end="")
    print()

    # Теперь печатаем сначала ребро, а затем значение (0 / 1)
    for start_point in graph.keys():
        for end_point in graph_copy[start_point]:
            print(f"{start_point}<->{end_point}\t", end="")
            # Тут печатаем 0/1 для каждого из значений
            for point_name in graph.keys():
                if point_name in (start_point, end_point):
                    print("1\t", end="")
                else:
                    print("0\t", end="")
            print()
            # Исключаем start_point из списка точек end_point, чтобы рёбра не выводились дваждыё
            graph_copy[end_point].remove(start_point)