import random
from typing import List


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
        field[x][y] = 5

    return field


def print_field(field: list):
    for i in field:
        txt = ""
        for j in i:
            txt = txt + str(j) + " "
        print(txt)


if __name__ == "__main__":
    field = generate_field(2, 10, 10, 10)
    print_field(field)
