# Тут ищется самый короткий маршрут
def shortest_route_search(graph: dict):
    cur_path = []

    a = input("Введите точку А:")
    if a not in graph:
        print("Точка A не найдена в графе( Попробуйте ещё раз!")
        return
    b = input("Введите точку B:")
    if b not in graph:
        print("Точка B не найдена в графе( Попробуйте ещё раз!")
        return

    cur_path.append(a)
    cur = a
    depth = {a: 0}

    cur_len = 0
    min_point_len = {a: 0}
    min_point_path = {a: [a]}

    while True:
        print("DEBUG: \n\tPath:", cur_path, "\n\tCur:", cur, "\n\tDepth:", depth, "\n\tmin_point_len:", min_point_len, "\n\tmin_point_path:", min_point_path)

        # Тут идём назад, если на текущей точке уже всё посмотрели
        if len(graph[cur]) == depth[cur]:
            cur_path.remove(cur_path[len(cur_path) - 1])
            if len(cur_path) == 0:
                break
            cur = cur_path[len(cur_path) - 1]
            cur_len -= 1
        # Тут идём вперёд к тем точкам, где мы ещё не были
        else:
            # Отмечаем, что в эту сторону мы с этой точки уже пробовали ходить
            depth[cur] += 1
            point_to_go = graph[cur][depth[cur] - 1]
            # Если нас там пока не было, или есть возможность сходить побыстрее
            if point_to_go not in min_point_len or min_point_len[point_to_go] > cur_len + 1:
                cur = point_to_go
                cur_len += 1
                cur_path.append(cur)
                min_point_len[cur] = cur_len
                min_point_path[cur] = list(cur_path)

                if cur not in depth:
                    depth[cur] = 0

    if b in min_point_path:
        print("Путь найден:", min_point_path[b])
        print("Количество шагов:", min_point_len[b])
    else:
        print("Пути нет! Попробуйте ещё раз!")