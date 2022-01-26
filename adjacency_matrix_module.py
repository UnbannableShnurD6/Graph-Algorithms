# Тут строится матрица смежности.
def adjacency_matrix(graph: dict):
    # Сначала печатаем столбцы
    print("\t", end="")
    for point_name in graph.keys():
        print(point_name + "\t", end="")
    print()

    # Теперь печатаем сначала столбец, а затем значение (0 / 1)
    for raw_point_name in graph.keys():
        print(raw_point_name + "\t", end="")
        for column_point_name in graph.keys():
            if column_point_name in graph[raw_point_name]:
                print("1\t", end="")
            else:
                print("0\t", end="")
        print()
