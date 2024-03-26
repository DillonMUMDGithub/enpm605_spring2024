class Vehicle:
    """
    A class to represent a vehicle
    """
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
        
    def drive_forward(self):
        print(f"The {self.color} vehicle is driving.")
    
    def steer(self,angle):
        print(f"The {self.color} vehicle is steering {angle} degrees.")
    
    def honk(self):
        pass
    
if __name__ == "__main__":
    vehicle_blue = Vehicle("blue",2000)
    vehicle_red = Vehicle("red",1500)
    
    vehicle_red.drive_forward()
    vehicle_blue.drive_forward()
    vehicle_blue.steer(15)
    
    print(vehicle_red.weight)
    print(vehicle_blue.weight)