# Вам необходимо дополнить функцию point_factory, так
# чтобы она возвращала N точек (1, 1), (2, 2), …, (N, N).
# Функция принимает в качестве аргумента N и возвращает N
# объектов класса Point

from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    x: float
    y: float


def point_factory(n: int) -> List[Point]:
    return [Point(i + 1, i + 1) for i in range(n)]


if __name__ == "__main__":
    print(point_factory(8))
