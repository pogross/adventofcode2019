from typing import List, Tuple
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "x, y")

X_MOVES = {"R": 1, "L": -1, "U": 0, "D": 0}
Y_MOVES = {"R": 0, "L": 0, "U": 1, "D": -1}


def _parse_input() -> Tuple[List[str]]:
    with open("input.txt", "r", encoding="utf-8") as f:
        return tuple(line.split(",") for line in f.read().splitlines())


def manhattan_distance(c1: Coordinate, c2: Coordinate):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)


def generate_route(cable: List[str], central_port: Coordinate) -> List[Coordinate]:
    """ Complete enumeration, sorry :( """

    route = [central_port]
    for step in cable:
        direction = step[0]
        step = int(step[1:])

        for _ in range(step):
            predecessor = route[-1]
            successor = Coordinate(
                predecessor.x + X_MOVES[direction], predecessor.y + Y_MOVES[direction]
            )
            route.append(successor)

    return route


def find_crossings(first_route, second_route, central_port) -> List[Coordinate]:
    crossings = list(set(first_route).intersection(second_route))
    crossings.remove(central_port)
    return crossings


def crossed_wires(cable1: List[str], cable2: List[str]) -> int:
    central_port = Coordinate(0, 0)

    first_route = generate_route(cable1, central_port)
    second_route = generate_route(cable2, central_port)

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
