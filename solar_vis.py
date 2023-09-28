# coding: utf-8
# license: GPLv3

"""Visualization module.
Screen coordinates are not used anywhere except in this module.
Functions that create graphical objects and move them on the screen
accept physical coordinates.
"""

header_font = "Arial-16"
"""Font in the header"""

window_width = 800
"""Window width"""

window_height = 800
"""Window height"""

scale_factor = None
"""Scaling of screen coordinates relative to physical ones.
Type: float
Measure: number of pixels per meter."""


def calculate_scale_factor(max_distance):
    """Calculates the value of the global variable **scale_factor** based on the given characteristic length"""
    global scale_factor
    scale_factor = 0.4 * min(window_height, window_width) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Returns the screen **x** coordinate based on the model **x** coordinate.
    Takes a float and returns an integer.
    In case the **x** coordinate goes beyond the screen, it returns
    a coordinate outside the canvas.

    Parameters:

    **x** - model's x-coordinate.
    """

    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """Returns the screen **y** coordinate based on the model **y** coordinate.
    Takes a float and returns an integer.
    In case the **y** coordinate goes beyond the screen, it returns
    a coordinate outside the canvas.
    The direction of the axis is reversed so that in the model, the **y** axis points upward.

    Parameters:

    **y** - model's y-coordinate.
    """

    return int(y * scale_factor) + window_width // 2


def create_star_image(space, star):
    """Creates the displayed star object.

    Parameters:

    **space** - canvas for drawing.
    **star** - star object.
    """

    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """Creates the displayed planet object.

    Parameters:

    **space** - canvas for drawing.
    **planet** - planet object.
    """

    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """Creates text on the canvas with the name of the celestial body system.
    If the text already exists, updates its content.

    Parameters:

    **space** - canvas for drawing.
    **system_name** - name of the celestial body system.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """Moves the displayed object on the canvas.

    Parameters:

    **space** - canvas for drawing.
    **body** - the body to be moved.
    """
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2 * r, window_height + 2 * r)  # place it outside the window
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
