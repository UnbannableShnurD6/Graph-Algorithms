from articulation_points_module import articulation_points
from brige_search_module import brige_search
from graph_connectivity_module import graph_connectivity
from route_search_module import route_search
from adjacency_matrix_module import adjacency_matrix
from incidence_matrix_module import incidence_matrix
from shortest_route_module import shortest_route_search

avilable_algos = [
    ["Матрица смежности", adjacency_matrix],
    ["Матрица инцидентности", incidence_matrix],
    ["Поиск маршрута", route_search],
    ["Поиск кратчайшего пути", shortest_route_search],
    ["Проверка на связность", graph_connectivity],
    ["Поиск мостов", brige_search],
    ["Поиск точек сочленения", articulation_points],
    ["Выход", lambda _: exit(0)]
]

if __name__ == '__main__':
    print("Привет! Сейчас нужно будет задать граф с клавиатуры.\n")

    is_graph_oreinted = int(input("Подскажите, граф будет ореинтирован?\n1 - Да, 2 - Нет.\n"))
    if is_graph_oreinted not in (1, 2):
        raise Exception("Неправильное значение")
    elif is_graph_oreinted == 1:
        is_graph_oreinted = True
    elif is_graph_oreinted == 2:
        is_graph_oreinted = False

    print("Напишите, какие точки с какими связаны в следующем формате: a->b.\n"
          "Имя точки может быть произвольным. Для завершения ввода просто отправьте пустуб строчку.\n")

    graph = {}
    input_message = "Введите новую связь в виде a->b:\n"
    input_str = input(input_message)

    while len(input_str):
        if input_str.count("->") != 1:
            print("Некорректный формат ввода. " + input_message)
            input_str = input(input_message)
            continue

        start_point, end_point = input_str.split("->")
        if start_point not in graph:
            graph[start_point] = []
        if end_point not in graph:
            graph[end_point] = []
        graph[start_point].append(end_point)
        if not is_graph_oreinted:
            graph[end_point].append(start_point)

        input_str = input(input_message)

    print("res: ", graph)

    print("Отлично! Граф загружен.\n"
          "Теперь давайте решим, что будем с ним делать:\n")

    while True:
        iter = 1
        for descr, _ in avilable_algos:
            print(f"{iter}\t: {descr}")
            iter += 1

        algo = int(input("Выберете необходимый сценарий: "))
        if len(avilable_algos) < algo or algo <= 0:
            print("Попробуйте ещё раз.\n")
            continue

        avilable_algos[algo - 1][1](graph)






