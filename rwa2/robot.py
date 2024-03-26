"""
This module contains the functions that control the robot's movement.
"""

def move_forward(Position, Orientation):
    """_Moves the robot forwards and updates its position based upon its orientation_

    Args:
        Position (_list_): _A 2 element list of strings indicating the current position of the robot_
        Orientation (_string_): _A string of either "up" "down" "left" or "right indicating the orientation_

    Returns:
        _list_: _2 element list with the position of the robot following a move_
    """
    #Add, or subtract from the first index, moving up or down based on the orientation
    if Orientation == "up":
        Post_move = [Position[0]-1,Position[1]]   
    if Orientation == "down":
        Post_move = [Position[0]+1,Position[1]] 
    #Add, or subtract from the second index, moving left or right based on the orientation     
    if Orientation == "left":
        Post_move = [Position[0],Position[1]-1]  
    if Orientation == "right":
        Post_move = [Position[0],Position[1]+1]
    #Ensuring that the robot doesn't exceed the left or right limits    
    if (Post_move[0]==4) or (Post_move[0]==-1):
        Post_move[0] = Position[0]  
        return Post_move
    #Ensuring that the robot doesn't exceed the top or bottom limits 
    if (Post_move[1]==4) or (Post_move[1]==-1):
        Post_move[1] = Position[1]  
        return Post_move                 
    return(Post_move)

def move_backward(Position, Orientation):
    """_Moves the robot forwards and updates its position based upon its orientation_

    Args:
        Position (_list_): _A 2 element list of strings indicating the current position of the robot_
        Orientation (_string_): _A string of either "up" "down" "left" or "right indicating the orientation_

    Returns:
        _list_: _2 element list with the position of the robot following a move_
    """
    #Add, or subtract from the first index, moving up or down based on the orientation
    if Orientation == "up":
        Post_move = [Position[0]+1,Position[1]]   
    if Orientation == "down":
        Post_move = [Position[0]-1,Position[1]]
    #Add, or subtract from the second index, moving left or right based on the orientation      
    if Orientation == "left":
        Post_move = [Position[0],Position[1]+1]  
    if Orientation == "right":
        Post_move = [Position[0],Position[1]-1]
    #Ensuring that the robot doesn't exceed the left or right limits
    if (Post_move[0]==4) or (Post_move[0]==-1):
        Post_move[0] = Position[0]
        print("Cannot exit the maze!")
        print(Post_move)   
        return Post_move
    #Ensuring that the robot doesn't exceed the top or bottom limits
    if (Post_move[1]==4) or (Post_move[1]==-1):
        Post_move[1] = Position[1]
        print("Cannot exit the maze!")
        print(Post_move)   
        return Post_move  
    
    print(Post_move)       
    return(Post_move)    


def turn_left(Orientation):
    """_Updates the orientation of the robot to turn left depending on its previous position and returns the new orientation_

    Args:
        Orientation (_string_): _a string, either "up", "down", left' or "right" describing robot orientation_
    """
    #Conditional results of turning left from all possible starting orientations
    if Orientation=="up":
        NewOrient = "left"
    if Orientation=="down":
        NewOrient = "right"
    if Orientation=="left":
        NewOrient = "down"
    if Orientation=="right":
        NewOrient = "up"
    #Returns the new orientation                
    return(NewOrient)

def turn_right(Orientation):
    """_Updates the orientation of the robot to turn left depending on its previous position_

    Args:
        Orientation (_string_): _a string, either "up", "down", left' or "right" describing robot orientation_
    """
    #Conditional results of turning right from all possible starting orientations
    if Orientation=="down":
        NewOrient = "left"
    if Orientation=="up":
        NewOrient = "right"
    if Orientation=="right":
        NewOrient = "down"
    if Orientation=="left":
        NewOrient = "up"   
    #reutrns the new orientation             
    return(NewOrient)

def update_robot_orientation(orientation):
    """_A function to update the emoji representation of the robot depending on the orientation and returns the new orientation_

    Args:
        orientation (_string_): _a string, either "up", "down", left' or "right" describing robot orientation_
    """
    #conditional on orientation, assign the proper emoji
    if orientation=="up":
        ROBOT = "⏫"
    if orientation=="down":
        ROBOT = "⏬"
    if orientation=="left":
        ROBOT = "⏪"
    if orientation=="right":
        ROBOT = "⏩"
    #Returns the proper emoji for robot orientation
    return(ROBOT)