# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Newton's gravitational constant G"""


def calculate_force(body, space_objects):
    """Calculates the force acting on a body.

    Parameters:

    **body** - the body for which to calculate the acting force.
    **space_objects** - a list of objects that exert an influence on the body.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # A body doesn't exert gravitational force on itself!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        f = gravitational_constant * body.m * obj.m / r ** 2
        body.Fx += -f * (body.x - obj.x) / r
        body.Fy += -f * (body.y - obj.y) / r


def move_space_object(body, dt):
    """Moves a body according to the force acting on it.

    Parameters:

    **body** - the body to be moved.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.x += dt * (body.Vx + body.Vx + ax * dt) / 2
    body.Vx += ax * dt
    body.y += dt * (body.Vy + body.Vy + ay * dt) / 2
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Recalculates the coordinates of objects.

    Parameters:

    **space_objects** - a list of objects for which to recalculate coordinates.
    **dt** - time step
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
