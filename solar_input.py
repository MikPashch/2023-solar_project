# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Reads data about celestial objects from a file, creates the objects themselves, 
        and initiates the creation of their graphical representations.

    Parameters:

    **input_filename** — the name of the input file.
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # Skip empty lines and comment lines.
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Parses data about a star from a string.
    The input string should have the following format:
    Star <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>
        
    Here, (x, y) are the star's coordinates, and (Vx, Vy) are its velocities.
    Example string:
    Star 10 red 1000 1 2 3 4
    
    Parameters:

    **line** — a string containing the star's description.
    **star** — the star object..
    """

    parameters = line.split()
    star.R = float(parameters[1])
    star.color = parameters[2]
    star.m = float(parameters[3])
    star.x = float(parameters[4])
    star.y = float(parameters[5])
    star.Vx = float(parameters[6])
    star.Vy = float(parameters[7])


def parse_planet_parameters(line, planet):
    """Parses data about a planet from a string.
    The input string should have the following format:
    Planet <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>

    Here, (x, y) are the planet's coordinates, and (Vx, Vy) are its velocities.
    Example string:
    Planet 10 red 1000 1 2 3 4

    Parameters:

    **line** — a string containing the planet's description.
    **planet** — the planet object.
    """

    parameters = line.split()
    planet.R = float(parameters[1])
    planet.color = parameters[2]
    planet.m = float(parameters[3])
    planet.x = float(parameters[4])
    planet.y = float(parameters[5])
    planet.Vx = float(parameters[6])
    planet.Vy = float(parameters[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Saves data about celestial objects to a file.
    The lines should have the following format:
    Star <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>
    Planet <radius in pixels> <color> <mass> <x> <y> <Vx> <Vy>"

    Parameters:

    **output_filename** — the name of the input file.
    **space_objects** — a list of planet and star objects.
    """

    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write("%s %d %s %f %f %f %f %f\n" % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx,
                                                          obj.Vy))
    with open('stats.txt', 'w') as stat:
        i = 0
        for obj in space_objects:
            if obj.type == 'planet':
                i += 1
                for j in range(3):
                    for element in obj.statistic[j]:
                        stat.write((str(element) + ' '))
                    stat.write('\n')
                stat.write('end\n')


def read_statistic(in_filename):
    stat_arr = []
    stat_temp = [[], [], []]
    i = 0
    with open(in_filename) as input_file:
        for line in input_file:
            split_line = line.split()
            if split_line[0] == 'end':
                stat_arr.append(stat_temp)
                stat_temp = [[], [], []]
                i = 0
            else:
                for element in split_line:
                    stat_temp[i].append(float(element))
                i += 1
    return stat_arr


if __name__ == "__main__":
    print("This module is not for direct call!")
