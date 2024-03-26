"""
This module contains the maze and the robot's initial position, as well as functions to print the maze and move the robot.
"""
from robot import update_robot_orientation

# Constants
# Here are all the emojis: "💥", "🏁", "⏫", "⏩", "⏪", "⏬", "🚧"
EMPTY = "  "
BOOM = "💥"
OBSTACLE = "🚧"
GOAL = "🏁"
ROBOT = "⏫"
HORIZONTAL_WALL = "──"
VERTICAL_WALL = "│"
CORNER = "┼"

# Define the size of the maze
MAZE_SIZE = 4

# Define the maze as a 2D list
maze = [[EMPTY] * MAZE_SIZE for _ in range(MAZE_SIZE)]
# Rewrite the previous line using for loops


# Define the robot's initial position
robot_position = [2, 3]  # [row, column]
robot_orientation = "up"

# Define the obstacles' positions
obstacle_positions = [[1, 1], [2, 2], [3, 3]]

# Define the goal position
goal_position = [3, 2]

# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

maze[robot_position[0]][robot_position[1]] = ROBOT
maze[goal_position[0]][goal_position[1]] = GOAL


# Function to print the maze
def print_maze():
    """_Function to print the maze with the included robot, obstaces, and goal as previously established_
    """
    # Print top boundary
    print("┌" + "─" * (MAZE_SIZE * 3 - 1) + "┐")

    for i, row in enumerate(maze):
        # Print left boundary
        print(VERTICAL_WALL, end="")

        # Print cell contents
        for j, cell in enumerate(row):
            print(cell, end="")
            # Print vertical wall if not in the last column
            if j < MAZE_SIZE - 1:
                print(VERTICAL_WALL, end="")

        # Print right boundary
        print(VERTICAL_WALL)

        # Print horizontal wall between rows (except for the last row)
        if i < MAZE_SIZE - 1:
            print("├" + "─" * (MAZE_SIZE * 3 - 1) + "┤")

    # Print bottom boundary
    print("└" + "─" * (MAZE_SIZE * 3 - 1) + "┘")
    
    

def update_maze(robot_position,previous_position,robot_orientation,previous_orientation):
    """_A function to update the map based on the position of the robot, prints the map after running_

    Args:
        robot_position (_list_): _A 2 element list of strings indicating the new position of the robot_
        previous_position (_list_): _A 2 element list of strings indicating the previous position of the robot_
        robot_orientation (_string_): _A string of either "up" "down" "left" or "right indicating the new orientation_
        previous_orientation (_string_): _A string of either "up" "down" "left" or "right indicating the previous orientation_
    """
#Updates the directional emoji accotding to the output of the update_robot_orientation function    
    ROBOT = update_robot_orientation(robot_orientation)
# Define the obstacles' positions
    obstacle_positions = [[1, 1], [2, 2], [3, 3]]
    status = ""
# Define the goal position
    goal_position = [3, 2]
# Place obstacles, the robot, and the goal in the maze
    for obstacle in obstacle_positions:
        maze[obstacle[0]][obstacle[1]] = OBSTACLE

    maze[goal_position[0]][goal_position[1]] = GOAL
#Replace the previous space with an open space following a move
    if (previous_orientation == robot_orientation) and (previous_position !=robot_position):
        maze[previous_position[0]][previous_position[1]] = "  "
#Checks if the robot has reached the position of the GOAL
    if robot_position == goal_position:
        maze[robot_position[0]][robot_position[1]] = GOAL
        print("Conratulations! you solved the maze")
        status = "victory"
#Checks if the robot has interacted with an obstacle 
    elif robot_position in obstacle_positions:
        maze[robot_position[0]][robot_position[1]] = BOOM
        print("BOOM! You hit an obstacle")
        status = "failure"
#If not interacting with an obstacle or the goal, place the robot at its position                
    else:
        maze[robot_position[0]][robot_position[1]] = ROBOT
#Print the maze        
    print_maze()
    return status

if __name__ == "__main__":
    print_maze()