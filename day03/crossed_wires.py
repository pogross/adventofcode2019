from typing import List, Tuple
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "x, y")


def _parse_input() -> Tuple[List[str]]:
    with open("input.txt", "r", encoding="utf-8") as f:
        return tuple(line.split(",") for line in f.read().splitlines())


def manhattan_distance(c1: Coordinate, c2: Coordinate):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def generate_cable_route(cable: List[str]) -> List[Coordinate]:
    """ Sorry brute-force :( """

    route = [Coordinate(0, 0)]
    for step in cable:
        direction = step[0]
        step = int(step[1:])

        for _ in range(step):
            origin = route[-1]
            if direction == "R":
                next_coord = Coordinate(origin.x + 1, origin.y)
            if direction == "L":
                next_coord = Coordinate(origin.x - 1, origin.y)
            if direction == "U":
                next_coord = Coordinate(origin.x, origin.y + 1)
            if direction == "D":
                next_coord = Coordinate(origin.x, origin.y - 1)

            route.append(next_coord)

    return route


def find_crossings(first_route, second_route, central_port):
    crossings = list(set(first_route).intersection(second_route))
    crossings.remove(central_port)
    return crossings


def crossed_wires(cable1: List[str], cable2: List[str]) -> int:
    central_port = Coordinate(0, 0)

    first_route = generate_cable_route(cable1)
    second_route = generate_cable_route(cable2)

    crossings = find_crossings(first_route, second_route, central_port)

    closest_distance = min(
        manhattan_distance(crossing, central_port) for crossing in crossings
    )

    fewest_steps = min(
        first_route.index(crossing) + second_route.index(crossing)
        for crossing in crossings
    )

    return closest_distance, fewest_steps


if __name__ == "__main__":
    data = _parse_input()
    closest_distance, fewest_steps = crossed_wires(*data)
    print(f"Closest intersection distance = {closest_distance}")
    print(f"Fewest combined steps = {fewest_steps}")
