# Тут ищется маршрут (не обязательно самый короткий!) поиском в глубину
def route_search(graph: dict, a=None, b=None):
    viewed = []
    path = []

    isSilence = a and b

    if a is None:
        a = input("Введите точку А:")
        if a not in graph:
            print("Точка A не найдена в графе( Попробуйте ещё раз!")
            return
    if b is None:
        b = input("Введите точку B:")
        if b not in graph:
            print("Точка B не найдена в графе( Попробуйте ещё раз!")
            return

    path.append(a)
    viewed.append(a)
    cur = a
    depth = {a: 0}

    while cur != b:
        # Тут идём назад, если на текущей точке уже всё посмотрели
        if len(graph[cur]) == depth[cur]:
            path.remove(path[len(path) - 1])
            if len(path) == 0:
                if not isSilence:
                    print("Пути нет! Попробуйте ещё раз!")
                return
            cur = path[len(path) - 1]
        # Тут идём впедёд к тем точкам, где мы ещё не были
        else:
            depth[cur] += 1

            # Если нас там пока не было
            if graph[cur][depth[cur] - 1] in viewed:
                continue
            # Переход на следующий элемент
            cur = graph[cur][depth[cur] - 1]
            # Элемент становится последним элеменом пути
            path.append(cur)
            if cur not in depth:
                depth[cur] = 0
            if cur not in viewed:
                viewed.append(cur)

    if not isSilence:
        print("Путь найден:", path)
    return path

