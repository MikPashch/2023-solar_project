# Team programming project "Solar System"

Large projects are typically developed by teams of programmers, so it's important to learn how to work on code collaboratively. Techniques like pair programming are commonly used, although a well-structured division of tasks among team members is also essential.

## Task
### Legend
A group of two programmers was working on the "Solar System" project. Their task was to model and visualize the motion of planets in a flat approximation for the Solar System or a similar system. The user interface should allow starting and pausing the passage of time. Collisions between planets or with the Sun are not required to be simulated. Initial data about the positions of planets, their masses, and initial velocities are read from a file. Upon the user's request, data about the current positions, masses, and velocities of the planets should be saved to a file.

However, both programmers suddenly resigned under unknown circumstances. You have been called in to save the situation and complete the program on time. Fortunately, the project had already been designed and well-documented.

### Modularization
The program should be divided into five modules:

- `solar_main.py` — the main module
- `solar_objects.py` — description of objects
- `solar_model.py` — module responsible for modeling physical objects
- `solar_vis.py` — module responsible for the user interface
- `solar_input.py` — module implementing reading and writing to configuration files

### Role Assignment
- Programmer A — Senior programmer, team lead. Responsibilities: `solar_main.py`, `solar_objects.py`, `solar_vis.py`
- Programmer B — Second programmer. Responsibilities: `solar_model.py`, `solar_input.py`

Remember that development should proceed step by step with each commit ensuring functionality.

## Programmer A's Plan
### Task Assignment
The main task for the team lead is to organize work. The workload for actual programming is lower.

It seems that everything has been done in the modules `solar_main.py` and `solar_objects.py`, and no corrections are needed. The `solar_vis` module, however, requires substantial adjustments.

#### Stage 0
Start by forking the repository to your own GitHub account (use the "Fork" button in the top right corner) and grant commit access to your subordinate programmer (repo -> settings -> collaborators -> add collaborator).

The project is located in the repository `solar_project`.

After that, clone the forked repository to both computers: team lead and the second programmer.

#### Stage 1
Correct the `scale_y` function and the `create_planet_image` function in the `solar_vis.py` module.

#### Stage 2
Assist the second programmer by working together as a pair. Review their code and test the project for errors.

## Programmer B's Plan
### Task Assignment
In the `solar_model.py` module, there is no computation scheme specified. The `solar_input.py` module does not implement reading and writing to files.

#### Stage 0
Make sure the team lead has forked correctly and clone their forked repository. Ensure that commit access rights are in place. You can make a trivial edit, commit it, and push it to GitHub.

#### Stage 1
Correct the file reading functions: `parse_star_parameters` and `parse_planet_parameters`. These two functions should correctly populate the fields of already created objects of type Star and Planet, respectively.

#### Stage 2
Fix the computations in the physical model, the `calculate_force` function, and `move_space_object`.

#### Stage 3
Correct the file writing function: `write_space_objects_data_to_file`.
