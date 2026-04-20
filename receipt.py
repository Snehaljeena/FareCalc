import datetime 
from exceptions import FareError

def user_input():
    try:
        distance=float(input("Enter Total Distance(km):"))
        if distance<=0:
            raise FareError("Distance must not be negative or zero")
        
        time=int(input("Enter hours(0-24):"))
        if not(time>=0 and time<=23):
            raise FareError("Invalid Timing")
        
        vehicle=input("Enter the type of vehicle (Economy/Premium/SUV): ").strip()

        return distance,time,vehicle
    
    except ValueError:
        raise FareError("Invalid input")

def print_receipt(distance,time,vehicle,fare):
    current_time=datetime.datetime.now()

    print("  RECEIPT  ")
    print(f"Time: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Distance: {distance:.2f} km")
    print(f"Vehicle type: {vehicle.capitalize()}")
    print(f"Hour: {time}:00")
    print(f"Total Fare: {fare:.2f}")



  
    


