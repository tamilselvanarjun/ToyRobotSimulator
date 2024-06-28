# Toy Robot Simulator

## Description

The Toy Robot Simulator is a simple application that simulates a toy robot moving on a 5x5 grid tabletop. The robot can be placed on the table, moved forward, and rotated left or right. The application ensures the robot does not fall off the table.

## Features

- The robot can be placed at a specific position on the table and face a specific direction (NORTH, SOUTH, EAST, WEST).
- The robot can move one unit forward in the direction it is currently facing.
- The robot can rotate left or right, changing its facing direction without changing its position.
- The robot's position and facing direction can be reported.

## Cloning the Repository

To clone the repository, run the following command:

```
git clone https://github.com/tamilselvanarjun/ToyRobotSimulator.git
```
Then navigate to the project directory:

```
cd ToyRobotSimulator
```

### Running the Application

#### There are two ways to run the application:

1. Save the commands in a file, e.g., `commands.txt`.

Run the application and pass the file as input:

```
python simulator.py commands.txt
```

2. Using Standard Input from command line:

Run the application and enter commands 
interactively. Type 'END' to finish input:

Example of interactive input:

```

C:\Users\Tamil\Simulator>python simulator.py
Enter commands for the Toy Robot Simulator. Type 'END' to finish.
PLACE 0,0,NORTH
LEFT
REPORT
END
```

## Commands

The application accepts the following commands:

- `PLACE X,Y,F` - Places the robot at the specified position (X, Y) facing the specified direction (F).
- `MOVE` - Moves the robot one unit forward in the direction it is currently facing.
- `LEFT` - Rotates the robot 90 degrees to the left.
- `RIGHT` - Rotates the robot 90 degrees to the right.
- `REPORT` - Outputs the robot's current position and facing direction.

## Constraints

- The table is a 5x5 grid.
- The robot must not fall off the table. Any movement that would result in the robot falling off the table is ignored.
- The first valid command must be a `PLACE` command.
- Subsequent commands are ignored until a valid `PLACE` command is received.