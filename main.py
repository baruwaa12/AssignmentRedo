

#===============

def bagCost(FlightSpec):
  bagCost = 0
  numOfBags = int(FlightSpec[4])
  
  if numOfBags <= 1:
    bagCost = bagCost
    print("This is the bag cost: ", bagCost)
  else:
    bagCost = (numOfBags - 1) * 20
    print("This is the bag cost: ", bagCost)
    
  return bagCost

#================

def getFinalBasicFlightCost(FlightSpec):
  BasicFlightCostAMS = 150
  BasicFlightCostGLA = 80
  FinalBasicFlightCost1 = 0
  FinalBasicFlightCost2 = 0
  SeatType = FlightSpec[11]
  destination = FlightSpec[0:3]
  passAge = int(FlightSpec[6:8])
  
  
  
  if destination == "GLA":
    if passAge <= 15:
      FinalBasicFlightCost1 = BasicFlightCostGLA / 2
      print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost1)
    else:
      FinalBasicFlightCost1 = BasicFlightCostGLA
      print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost1)
      
  
  if destination == "AMS":
    if passAge <= 15:
      FinalBasicFlightCost1 = BasicFlightCostAMS / 2
      print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost1)
    else:
      FinalBasicFlightCost1 = BasicFlightCostAMS
      print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost1)

  
  if SeatType == "F":
    FinalBasicFlightCost2 = FinalBasicFlightCost1 * 6
    print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost2)
    return FinalBasicFlightCost2
    
  elif SeatType == "E":
    FinalBasicFlightCost1 = FinalBasicFlightCost1
    print("This is the FinalBasicFlightCost: ", FinalBasicFlightCost2)
    
  return FinalBasicFlightCost1 

#===============

def getChosenMeal(FlightSpec):
  MealCostS = 10
  MealCostV = 12
  FinalMealCost = 0
  MealChosen = FlightSpec[9]
  passAge = int(FlightSpec[6:8])
  
  if MealChosen == "S":
    if passAge <= 15:
      FinalMealCost = MealCostS - 2.50
      print("This is the FinalMealCost: ", FinalMealCost)
    else:
      FinalMealCost = MealCostS

  if MealChosen == "V":
    if passAge <= 15:
      FinalMealCost = MealCostV - 2.50
      print("This is the FinalMealCost: ", FinalMealCost)
    else:
      FinalMealCost = MealCostV
      print("This is the FinalMealCost: ", FinalMealCost)
      
  return FinalMealCost


#===============


def totalFlightCost():
  
  FlightSpec = input("Please enter your specfication? ")
  result = bagCost(FlightSpec) + getFinalBasicFlightCost(FlightSpec) + getChosenMeal(FlightSpec)
  print(result)
#===============




totalFlightCost()


