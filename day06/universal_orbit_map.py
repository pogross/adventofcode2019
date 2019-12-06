from typing import List
from collections import namedtuple

import networkx as nx
import matplotlib.pyplot as plt

Relation = namedtuple("Relation", "object orbiter")


def _parse_orbital_relations() -> List[Relation]:
    with open("input.txt", "r", encoding="utf-8") as f:
        return [Relation(*value.split(")")) for value in f.read().split("\n")]


def get_space_objects(orbital_relations):
    space_objects = {
        space_object for connection in orbital_relations for space_object in connection
    }
    return space_objects


def map_validator(orbital_relations: List[Relation]):

    space_objects = get_space_objects(orbital_relations)
    space_map = nx.DiGraph()
    space_map.add_nodes_from(space_objects)

    # directed edges pointing backwards object <- orbiter
    for relation in orbital_relations:
        space_map.add_edge(relation.orbiter, relation.object)

    count = 0
    for space_object in space_objects:
        direct_orbiters = list(space_map.neighbors(space_object))
        indirect_orbiters = [
            orbiter
            for orbiter in nx.descendants(space_map, space_object)
            if orbiter not in direct_orbiters
        ]
        count += len(direct_orbiters) + len(indirect_orbiters)

    return count


def map_navigator(orbital_relations: List[Relation]):

    space_objects = get_space_objects(orbital_relations)
    space_map = nx.Graph()  # this time not directed
    space_map.add_nodes_from(space_objects)

    for relation in orbital_relations:
        space_map.add_edge(relation.orbiter, relation.object)

    orbiter_lookup = {
        relation.orbiter: relation.object for relation in orbital_relations
    }
    sp = nx.shortest_path(space_map, orbiter_lookup["YOU"], orbiter_lookup["SAN"])

    # draw_shortest_path(space_map, sp)

    return len(sp) - 1  # only transfers not nodes


def draw_shortest_path(space_map, path):
    pos = nx.spring_layout(space_map)
    nx.draw(space_map, pos, node_color="green", with_labels=True)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(space_map, pos, nodelist=path, node_color="red")
    nx.draw_networkx_edges(space_map, pos, edgelist=path_edges, edge_color="black")
    plt.show()


if __name__ == "__main__":
    oc = _parse_orbital_relations()
    print(f"Number of direct and indirect orbits = {map_validator(oc)}")
    print(f"Shortest path to santa = {map_navigator(oc)}")
