max_weight_grams = float(120)
step_grams = float(10)

def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Payload weight must be greater than 0 grams.")
        #Accepted: AI suggested ValueError message: "Payload weight must be greater than 0 grams."
    elif weight_grams >= 0:
        flight_time = 180 - 0.1 * (weight_grams)
        #Edited: AI kept trying to change the formula to weight_grams * 0.1 instead of one in assignment.
    if flight_time <= 0:
        return 0
    elif flight_time > 0:    
        return flight_time

def flight_time_table(max_weight_grams,step_grams):
    print("Weight (grams)\t|\tFlight Time (seconds)")
    for weight in range(0, int(max_weight_grams) + 1, int(step_grams)):
        flight_time = calculate_flight_time(weight)
        print(f"{weight}\t\t|\t{flight_time:.2f}")
        #Rejected: AI suggested writing formula for flight time, instead of calling calculate_flight_time function.
    return


def main():
    flight_time_table(max_weight_grams, step_grams)

main()