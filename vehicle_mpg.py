print ("Welcome!")
print ("\tThis program is designed to evaluate how well your vehicle is doing in terms of fuel economy ")
print ("\tin miles per gallon (MPG) in order to help make a decision regarding the purchase of a newer vehicle,")
print ("\tone that gets better gas mileage, or not.")

print ("\nLets get started!")
user_name = input ("\nPlease enter your name. ")
vehicle_make = input("What is the make of your vehicle? ")
vehicle_model = input ("What is the model of your vehicle? ")
vehicle_year = input ("What is the year of your vehicle? ")
total_milesSTR = input ("What is the total number of miles you drove your vehicle during your evaluation? ")
total_gallonsSTR = input ("What is the total amount of gallons of gas your vehicle consumed during your evaluation? ")
cost_per_gallonSTR = input ("What is the US dollar amount you paid per gallon of gas? ")
user_location = input ("What is the location of the evaluation by city and state? ")

total_gallons = float(total_gallonsSTR)
total_miles = float(total_milesSTR)

cost_per_gallon = float(cost_per_gallonSTR)
cost_per_week = float(cost_per_gallon * total_gallons)
cost_per_year = float(cost_per_week * 52.1775)

total_kilometers = float(total_miles * 1.609344)
total_liters = float(total_gallons * 3.78541)

MPG = float(total_miles / total_gallons)
KPL = float(total_kilometers / total_liters)

print ("")

print ("\tA " + vehicle_year + " " + vehicle_make + " " + vehicle_model + " has been evaluated over the a course of a one week period in " + user_location +".")
print ("\tHere are the results:")


print("")

print ("\tThe vehicle has been driven a total number of" , total_miles , "miles.")
print ("\tThis is equivalent to " , total_kilometers , " kilometers.")

print ("")

print ("\tThe vehicle consumed" , total_gallons , "gallons of gasoline.")
print ("\tThis is equivalent to" , total_liters , "liters of gasoline." )
print ("")

print ("Therefore,")
print("")
print ("The total cost of fuel per year is " , cost_per_year , " US dollars.")

print ("")
print ("The vehicle has" , MPG , " miles per gallon (MPG).")
print ("This is equivalent to", KPL, " kilometers per liter (KPL).")

print ("")

if MPG < 30:
    print ("After reviewing the data provided, it is advised that you purchase a newer vehicle with a higher MPG.")

if MPG >= 30:
    print ("After reviewing the data provided, your MPG is of a sufficient value that you need not purchase a newer vehicle.")
