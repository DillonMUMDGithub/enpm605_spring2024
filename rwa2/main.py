"""
This is the main file which contains the entry point of your program.
"""

#Import the necessary functions and values from external files
from maze import print_maze, robot_orientation,robot_position,update_maze
from robot import move_forward,move_backward,turn_left,turn_right

def main():
    """_Main function to allow user input the move the robot throughout the maze, sonstantly printing the new updated mazes_
    """
    #Print the initial maze
    print("Initial Maze:")
    print_maze()
    #Establish initial position and orientation variables
    NewPos = robot_position
    NewOri = robot_orientation
    while True:
        #Request inout from the user with the instructions for operation
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")

        #Establish historical values for comparison in later functions
        OldPos = NewPos
        OldOri = NewOri
        #Move Forward, output assigned to NewPos from move_forward
        if action =='w':
            NewPos = move_forward(NewPos,NewOri)
        #Move Backwards, output assigned to NewPos from move_backward
        elif action =="s":
            NewPos = move_backward(NewPos,NewOri)
        #Turn Left, output assigned to NewOri from turn_left
        elif action =="a":
            NewOri = turn_left(NewOri)
        #Turn Right, output assigned to NewOri from turn_right
        elif action =="d":
            NewOri = turn_right(NewOri)
        #Option to quit the program
        elif action =="q":
            break
        #Condition to only allow the applicable inputs
        else:
            print("Invalid Input")    
        
        #Update the maze with the historical position and orientation and the new position and orientation
        #Outputs: A, a message of victory or failure
        A = update_maze(NewPos,OldPos,NewOri,OldOri)

        #Conditions to exit the loop if reaching the goal or striking an obstacle
        if A == "victory":
            break
        if A == "failure":
            break

        
# Run the main function
if __name__ == "__main__":
    main()
