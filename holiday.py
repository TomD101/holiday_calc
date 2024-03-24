# Holiday cost calculator

# Inputs for city_flight (create options), num_nights, rental_days (days hiring a car)

#city = ["London", "Barcelona", "Milan", "Prague", "Copenhagen"]
# Library of flight prices based on city


# Functions for hotel, plane and car rental costs
def hotel_cost (num_nights):
    hotel_price = 130.60
    return (hotel_price) * (num_nights)
# dictionary for cities and costs

flight_costs = {
        "Brussels": 65.50, 
        "Barcelona": 70.25, 
        "Milan": 70.79, 
        "Prague": 55.05,
        "Copenhagen": 79.99,
    }

def plane_cost(city_flight):
    
    #tried to get if else to validate city but couldn't get it to work
    #return flight_costs.get(city_flight)
    #if city_flight in flight_costs.keys:
    return flight_costs[city_flight]
    #else:
    #print("The destination entered is not available. Please choose again.")


# car_rental function based on days * daily cost
def car_rental (rental_days):
    car_cost = 35.75
    return car_cost * rental_days

# Input questions
city_flight = input (f"Where do you want to fly to? Your options are: {' / '.join(flight_costs.keys())}: ")
#if city_flight in flight_costs.keys():
if city_flight in flight_costs.keys():
    print ("Sorry, this destination is not available, please start again. ")
else:
    num_nights = int(input("How many nights is your trip? : "))
    rental_days = int(input("Hom many days do you need a rental car for? : "))
 
# Function for holiday total cost
def holiday_cost(num_nights, city_flight, rental_days):
# Returns - The total cost of the holiday (hotel + flight + car rental)
    hotel_price = hotel_cost(num_nights)
    plane_price = plane_cost(city_flight)
    car_price = car_rental(rental_days)
    total_cost = hotel_price + plane_price + car_price
    return total_cost

# Printouts of trip details and total costs
print(f"Your trip will cost £{plane_cost(city_flight)} for the flights,")
print(f"£{hotel_cost(num_nights)} for {num_nights} night(s) in a hotel,")
print(f"and £{(car_rental(rental_days))} for {rental_days} day(s) car rental.")
print(f"Total cost for your trip is £{holiday_cost(num_nights, city_flight, rental_days)}")


