import random
from typing import List, Tuple
from crimson import make_choice


def generate_field(player_count: int, coin_count: int, size_x: int, size_y: int) -> list[list[int]]:
    """

    :param player_count: count of players on field
    :param coin_count: count of coins
    :param size_x: x size
    :param size_y: y size
    :return: list with list`s
    """
    field = [[0] * size_y for _ in range(size_x)]  # Создаем пустое поле

    # Расставляем монеты
    for _ in range(coin_count):
        x = random.randint(0, size_x - 1)
        y = random.randint(0, size_y - 1)
        field[x][y] = 1

    # Расставляем стены
    wall_count = (size_x * size_y) // 4  # Вычисляем количество стен пропорционально размеру поля
    for _ in range(wall_count):
        x = random.randint(0, size_x - 1)
        y = random.randint(0, size_y - 1)
        while field[x][y] != 0:  # Проверяем, что место для стены свободно
            x = random.randint(0, size_x - 1)
            y = random.randint(0, size_y - 1)
        field[x][y] = -1

    # Расставляем игроков
    for i in range(player_count):
        x = random.randint(0, size_x - 1)
        y = random.randint(0, size_y - 1)
        while field[x][y] != 0:  # Проверяем, что место для игрока свободно
            x = random.randint(0, size_x - 1)
            y = random.randint(0, size_y - 1)
        field[x][y] = {"name": "bot name", "life": 10, "history": []}

        # Функция для проверки достижимости всех ячеек на поле
        def is_reachable(x, y, visited):
            if x < 0 or x >= size_x or y < 0 or y >= size_y or field[x][y] == -1 or visited[x][y]:
                return False
            visited[x][y] = True
            is_reachable(x + 1, y, visited)
            is_reachable(x - 1, y, visited)
            is_reachable(x, y + 1, visited)
            is_reachable(x, y - 1, visited)
            return True

        # Создаем массив visited для отслеживания посещенных ячеек
        visited = [[False] * size_y for _ in range(size_x)]

        # Проверяем достижимость всех ячеек на поле
        for i in range(size_x):
            for j in range(size_y):
                if field[i][j] != -1:
                    visited = [[False] * size_y for _ in range(size_x)]
                    if not is_reachable(i, j, visited):
                        field[i][j] = -1  # Метим ячейку как недостижимую

        return field

def print_field(field: list):
    for i in field:
        txt = ""
        for j in i:
            txt = txt + str(j) + " "
        print(txt)

def check_field(field:list[list]) -> tuple[bool, list[list]]:
    for i in range(len(field)):
        x = field[i]
        for j in range(len(x)):
            y = j
            if field[i][y] != 1 and field[i][y] != -1 and field[i][y] != 0:
                print(i, j)
                r = make_choice(i, y, field)
                print(r)
                field[i][j] = "up"
                if r == False:
                    return True, field
    return False, field



if __name__ == "__main__":
    field = generate_field(2, 10, 10, 10)
    print_field(field)
    check_field(field)