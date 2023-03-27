# coding: utf-8
# license: GPLv3


class Star:
    """Type data, describes the star.
    Included weight, coordinates, speed of star,
    radius in the pexels and color
    """

    type = "star"
    """type of initialization of planet"""

    m = 0
    """weight of the planet"""

    x = 0
    """coordinate by **x**"""

    y = 0
    """coordinate by **y**"""

    Vx = 0
    """speed by **x**"""

    Vy = 0
    """speed by **y**"""

    Fx = 0
    """force by **x**"""

    Fy = 0
    """force by **y**"""

    R = 5
    """radius of the star"""

    color = "red"
    """color of the star"""

    image = None
    """image of the planet"""


class Planet:
    """Type data, describes the planet.
    Included weight, coordinates, speed of planet,
    radius in the pexels and color
    """

    type = "planet"
    """type of initialization of planet"""

    m = 0
    """weight of the planet"""

    x = 0
    """coordinate by **x**"""

    y = 0
    """coordinate by **y**"""

    Vx = 0
    """speed by **x**"""

    Vy = 0
    """speed by **y**"""

    Fx = 0
    """force by **x**"""

    Fy = 0
    """force by **y**"""

    R = 5
    """radius of the planet"""

    color = "green"
    """color of the planet"""

    image = None
    """image of the planet"""
