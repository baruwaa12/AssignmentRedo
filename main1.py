## User enters Flight Specification - GLA 0 25 S E

flightSpec = str(input("Enter a flight specification? "))

print(flightSpec)

## Key Variables
passAge = int(flightSpec[6:8])
destination = str(flightSpec[0:3])
numOfBags = int(flightSpec[4])
MealChosen = str(flightSpec[9])

## Find the number of bags and calculate the bag cost

bagCost = 0

if numOfBags <= 1:
    bagCost = bagCost
else:
    bagCost = (numOfBags - 1) * 20
    print(bagCost)

print("bagCost: ", bagCost)

## Check for the destination
## Find out the current flight cost and see if the child discount can be applied
## Check an appropriate age has been given.
BasicFlightCostAMS = 150
BasicFlightCostGLA = 80
CurrentFlightCost = 0


if destination == "GLA":
  if passAge <= 15:
    CurrentFlightCost = BasicFlightCostGLA / 2
  else:
    CurrentFlightCost = BasicFlightCostGLA

if destination == "AMS":
  if passAge <= 15:
    CurrentFlightCost = BasicFlightCostAMS / 2
  else:
    CurrentFlightCost = BasicFlightCostAMS


## Find out what meal was chosen.
## Determine if a child discount can be applied to meal cost 
MealCostS = 10
MealCostV = 12
FinalMealCost = 0


if MealChosen == "S":
  if passAge <= 15:
    FinalMealCost = MealCostS - 2.50
    print(FinalMealCost)
  else:
    FinalMealCost = MealCostS

if MealChosen == "V":
  if passAge <= 15:
    FinalMealCost = MealCostV - 2.50
  else:
    FinalMealCost = MealCostV


## Determine the Seating Class and the final basic flight cost
SeatType = flightSpec[11]
FinalFlightCost = 0

if SeatType == "F":
  FinalBasicFlightCost = CurrentFlightCost * 6
else:
  FinalBasicFlightCost = CurrentFlightCost

print("FinalBasicFlightCost = ", FinalBasicFlightCost)