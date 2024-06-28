import sys

class ToyRobotSimulator:
    """
    A class to simulate a toy robot moving on a 5x5 grid tabletop.
    The robot can be placed, moved, and rotated on the table.

    Attributes:
        table_size (int): The size of the table (default is 5x5).
        x (int): The x-coordinate of the robot's position.
        y (int): The y-coordinate of the robot's position.
        f (str): The direction the robot is facing ('NORTH', 'EAST', 'SOUTH', 'WEST').
        directions (list): The list of valid directions.
    """

    def __init__(self):
        """
        Initializes the ToyRobotSimulator with a 5x5 table and no initial position or direction.
        """
        self.table_size = 5
        self.x = None
        self.y = None
        self.f = None
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def place(self, x, y, f):
        """
        Places the robot at the specified coordinates (x, y) and direction (f).

        Args:
            x (int): The x-coordinate for placing the robot.
            y (int): The y-coordinate for placing the robot.
            f (str): The direction the robot should face ('NORTH', 'EAST', 'SOUTH', 'WEST').

        Returns:
            None
        """
        if 0 <= x < self.table_size and 0 <= y < self.table_size and f in self.directions:
            self.x = x
            self.y = y
            self.f = f

    def move(self):
        """
        Moves the robot one unit forward in the direction it is currently facing.

        Returns:
            None
        """
        if self.x is not None and self.y is not None and self.f is not None:
            if self.f == 'NORTH' and self.y < self.table_size - 1:
                self.y += 1
            elif self.f == 'EAST' and self.x < self.table_size - 1:
                self.x += 1
            elif self.f == 'SOUTH' and self.y > 0:
                self.y -= 1
            elif self.f == 'WEST' and self.x > 0:
                self.x -= 1

    def left(self):
        """
        Rotates the robot 90 degrees to the left.

        Returns:
            None
        """
        if self.f is not None:
            self.f = self.directions[(self.directions.index(self.f) - 1) % 4]

    def right(self):
        """
        Rotates the robot 90 degrees to the right.

        Returns:
            None
        """
        if self.f is not None:
            self.f = self.directions[(self.directions.index(self.f) + 1) % 4]

    def report(self):
        """
        Reports the current position and direction of the robot.

        Returns:
            str: The current position and direction of the robot in the format "X,Y,F".
        """
        if self.x is not None and self.y is not None and self.f is not None:
            return f"{self.x},{self.y},{self.f}"
        return None

    def execute_command(self, command):
        """
        Executes a given command to control the robot.

        Args:
            command (str): The command to execute ('PLACE X,Y,F', 'MOVE', 'LEFT', 'RIGHT', 'REPORT').

        Returns:
            str: The result of the 'REPORT' command, if executed. Otherwise, None.
        """
        parts = command.strip().split()
        if parts[0] == 'PLACE' and len(parts) == 2:
            x, y, f = parts[1].split(',')
            self.place(int(x), int(y), f)
        elif parts[0] == 'MOVE':
            self.move()
        elif parts[0] == 'LEFT':
            self.left()
        elif parts[0] == 'RIGHT':
            self.right()
        elif parts[0] == 'REPORT':
            return self.report()
        return None

def main():
    """
    Main function to read commands from standard input or a file and execute them.

    Returns:
        None
    """
    robot = ToyRobotSimulator()
    
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            commands = file.readlines()
    else:
         # Read commands interactively
        print("Enter commands for the Toy Robot Simulator. Type 'END' to finish.")
        commands = []
        while True:
            command = input().strip()
            if command.upper() == 'END':
                break
            commands.append(command)

    for command in commands:
        output = robot.execute_command(command)
        if output:
            print(output)

if __name__ == "__main__":
    main()
