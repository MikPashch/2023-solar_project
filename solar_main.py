# coding: utf-8
# license: GPLv3

import tkinter
import pylab
import math
from tkinter.filedialog import *
from solar_vis import *
from solar_model import *
from solar_input import *

perform_execution = False
"""Cyclic calculation flag."""

physical_time = 0
"""Physical time elapsed since the start of the calculation.
Type: float"""

displayed_time = None
"""Time displayed on the screen.
Type: tkinter variable."""

time_step = None
"""Time step in the simulation.
Type: float."""

space_objects = []
"""List of celestial objects."""


def execution():
    """The execution function - runs cyclically, processing all celestial bodies and updating their positions on the screen.
    The cyclic execution depends on the value of the global variable 'perform_execution'.
    When 'perform_execution' is True, the function requests a timer-based call to itself with a time interval between 1 ms and 100 ms.
    """
    global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects, time_step.get())
    for body in space_objects:
        update_object_position(space, body)
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")

    star = None
    for obj in space_objects:
        if obj.type == "star":
            star = obj
    for obj in space_objects:
        if obj.type == "planet":
            obj.statistic[0].append(physical_time)
            obj.statistic[1].append(math.sqrt(obj.Vx ** 2 + obj.Vy ** 2))
            obj.statistic[2].append(math.sqrt((obj.x - star.x) ** 2 + (obj.y - star.y) ** 2))

    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Event handler for the Start button click.
    Starts the cyclic execution of the 'execution' function.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    execution()
    print('Started execution...')


def stop_execution():
    """Event handler for the Stop button click.
    Stops the cyclic execution of the 'execution' function.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """Opens a file selection dialog and calls the function to read celestial system parameters from the selected file. 
    The read objects are saved in the global list 'space_objects'.
    """
    global space_objects
    global perform_execution
    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # deletion of old planet images.
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

    for obj in space_objects:
        if obj.type == 'star':
            create_star_image(space, obj)
        elif obj.type == 'planet':
            create_planet_image(space, obj)
        else:
            raise AssertionError()


def save_file_dialog():
    """Opens a file selection dialog and calls the function to read celestial system parameters from the selected file. 
    The read objects are saved in the global list 'space_objects'.
    """

    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_space_objects_data_to_file(out_filename, space_objects)


def graph():
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    stat_arr = read_statistic(in_filename)

    print(stat_arr[0][2])

    for planet_stat in stat_arr:
        pylab.subplot(2, 2, 1)
        pylab.plot(planet_stat[0], planet_stat[1])
        pylab.title("absolute velocity depending to time")

        pylab.subplot(2, 2, 3)
        pylab.plot(planet_stat[0], planet_stat[2])
        pylab.title("distant to star depending to time")

        pylab.subplot(1, 2, 2)
        pylab.plot(planet_stat[2], planet_stat[1])
        pylab.title("absolute velocity depending on distant to star")

        pylab.show()


def main():
    """Main function of main module.
    Creates graphical design objects using the tkinter library: window, canvas, frame with buttons, and buttons.
    """

    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # The cosmic space is displayed on a Canvas type canvas.
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="white")
    space.pack(side=tkinter.TOP)
    # The bottom panel with buttons.
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)
    graph_button = tkinter.Button(frame, text="Graph", command=graph)
    graph_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')


if __name__ == "__main__":
    main()
