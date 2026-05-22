"""
IS 303 Midterm
Ellie Meredith
Road Trip

"""
#inputs
total_distance = int(input("Total Distance in miles: "))
fuel_efficiency = int(input("Vehicle fuel efficiency in miles per gallon: "))
price_per_gallon = float(input("Current gas price per gallon: "))
toll_pass_needed = input("Do you need a toll pass?(yes/no):").lower().strip() 

#processes
gallons_needed = total_distance / fuel_efficiency
gas_cost = gallons_needed * price_per_gallon

if toll_pass_needed == "yes":
    toll_cost = 15.00
else:
    toll_cost = 0.00

total_cost = gas_cost + toll_cost

#Outputs
print("--- Trip Cost Summary ---")
print(f"Distance: {total_distance} miles")
print(f"Gas needed: {gallons_needed:.2f} gallons")
print(f"Gas cost: ${gas_cost:.2f}")
print(f"Toll cost: ${toll_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")

if total_cost > 100:
    print("Consider carpooling to split the cost!")