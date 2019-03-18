from random import seed, sample, choice
from os import linesep
from string import punctuation
from math import sqrt
from itertools import product

SEED_NUMBER = 1024
seed(SEED_NUMBER)
MAP_SIZE = 100
all_possible_symbols = frozenset(punctuation+'GSFT ')


def define_possible_objects(choices=punctuation):
    chars = choices
    chars += 'G'
    chars += 'T'*3
    chars += 'F'*3
    return chars


def generate_object(itera, available_coordinates, occupied_coordinates):
    symbol = sample(itera, 1)
    coordinates = choice(available_coordinates)
    available_coordinates.remove(coordinates)
    occupied_coordinates.append(coordinates)
    return symbol, coordinates


def set_up():
    symbols1 = define_possible_objects(punctuation)
    symbols2 = define_possible_objects('^&*'*5)
    return symbols1, symbols2


def generate_available_coordinates(map_size):
    return list(product(range(map_size), range(map_size)))


def generate_empty_map(available_coordinates):
    world_map = dict()
    for i in available_coordinates:
        world_map[i] = ' '
    world_map[(0,0)] = 'S'
    return world_map


def get_unique_objects(world_map):
    return frozenset(world_map.values())


def symbols_not_used_in_world(symbols_in_world):
    return all_possible_symbols.difference(symbols_in_world)


def common_objects_encountered(world_1_objects, world_2_objects):
    return world_1_objects.intersection(world_2_objects)


def objects_encountered_in_world1_not_world2(world_1_objects, world_2_objects):
    return world_1_objects.difference(world_2_objects)


def objects_encountered_in_world2_not_world1(world_1_objects, world_2_objects):
    return world_2_objects.difference(world_1_objects)


def objects_encountered_in_both_worlds(world1_objects, world2_objects):
    return world1_objects.union(world2_objects)


def calculate_path_to_goal(sorted_object_list):
    output_list = list()
    for i in sorted_object_list:
        if i[2][0] in 'FT':
            output_list.append(i)
        elif i[2][0] in 'G':
            output_list.append(i)
            break

    return output_list


def display_world(world_map):
    map_string = ''
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            map_string += world_map[(i,j)]
        map_string += linesep
    return map_string


def calculate_euclidean_distance(coordinates):
    x,y = coordinates
    return int(sqrt(x**2 + y**2))


def populate_world_map(available_symbols, available_coordinates, occupied_coordinates, world_map):
    objects_encountered_list = list()
    while True:
        symbol, coordinates = generate_object(available_symbols, available_coordinates, occupied_coordinates)
        distance = calculate_euclidean_distance(coordinates)
        objects_encountered_list.append((distance, coordinates, symbol))
        world_map[coordinates] = symbol[0]
        if symbol[0] == 'G':
            break
    return sorted(objects_encountered_list)



def run_exploration():
    available_symbols1, available_symbols2 = set_up()

    available_coordinates1 = generate_available_coordinates(MAP_SIZE)
    available_coordinates2 = generate_available_coordinates(MAP_SIZE)
    occupied_coordinates1 = list()
    occupied_coordinates2 = list()

    world_map_1 = generate_empty_map(available_coordinates1)
    world_map_2 = generate_empty_map(available_coordinates2)

    explorer1_list = populate_world_map(available_symbols1, available_coordinates1, occupied_coordinates1, world_map_1)
    explorer2_list = populate_world_map(available_symbols2, available_coordinates2, occupied_coordinates2, world_map_2)

    print(explorer1_list)
    print(explorer2_list)

    path_list1 = calculate_path_to_goal(explorer1_list)
    print(path_list1)

    path_list2 = calculate_path_to_goal(explorer2_list)
    print(path_list2)

    display_world(world_map_1)
    display_world(world_map_2)
    world2_symbols = get_unique_objects(world_map_2)
    world1_symbols = get_unique_objects(world_map_1)
    print(world1_symbols)
    print(world2_symbols)


if __name__ == '__main__':
    run_exploration()
