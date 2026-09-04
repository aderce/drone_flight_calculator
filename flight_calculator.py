weight_grams = float(input("Enter the weight of the payload: "))
flight_time = calculate_flight_time(weight_grams)

def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Payload weight must be greater than 0 grams.")
        #AI suggested ValueError message: "Payload weight must be greater than 0 grams."
    elif weight_grams >= 0:
        flight_time = 180 - 0.1 * (weight_grams)
        #AI kept trying to change the formula to weight_grams * 0.1 instead of one in assignment.
    if flight_time <= 0:
        return 0
    elif flight_time > 0:    
        return flight_time