from configure import SURGE_RATE,PEAK_HOURS,RATES
from exceptions import FareError

def calculate(distance:float,time:int, vehicle:str)->float:
    vehicle=vehicle.upper()

    if vehicle not in RATES:
        raise FareError("Service Not Available")
    
    fare=distance*RATES[vehicle]

    if time in PEAK_HOURS:
        fare=fare*SURGE_RATE

    return fare