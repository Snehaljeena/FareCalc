from farecalculate import calculate
from exceptions import FareError
from receipt import user_input,print_receipt

def main():
    try:
        distance,time,vehicle=user_input()
        fare=calculate(distance,time,vehicle)
        print_receipt(distance,time,vehicle,fare)

    except FareError as e:
        print(f"Error: {e}")

if __name__ == "__main__": 
    main() 