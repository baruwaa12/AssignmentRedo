

#===============

def bagCost(FlightSpec):
  bagCost = 0
  if numOfBags <= 1:
    bagCost = bagCost
    print(bagCost)
  else:
    bagCost = (numOfBags - 1) * 20
    print(bagCost)
    
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
      print(FinalBasicFlightCost1)
    else:
      FinalBasicFlightCost1 = BasicFlightCostGLA
      print(FinalBasicFlightCost1)
      
  
  if destination == "AMS":
    if passAge <= 15:
      FinalBasicFlightCost1 = BasicFlightCostAMS / 2
      print(FinalBasicFlightCost1)
    else:
      FinalBasicFlightCost1 = BasicFlightCostAMS
      print(FinalBasicFlightCost1)

  
  if SeatType == "F":
    FinalBasicFlightCost2 = FinalBasicFlightCost1 * 6
    print(FinalBasicFlightCost2)
  elif SeatType == "E":
    FinalBasicFlightCost1 = FinalBasicFlightCost1
    print(FinalBasicFlightCost1)
    
  return FinalBasicFlightCost1

#===============

def getChosenMeal(FlightSpec):
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
  return FinalMealCost


#===============

def isFirstClass(FlightSpec):
  FinalBasicFlightCost = 0
  CurrentFlightCost = getCurrentFlightCost
  
  SeatType = FlightSpec[11]
  
  if SeatType == "F":
    FinalBasicFlightCost = CurrentFlightCost * 6
  elif SeatType == "E":
    FinalBasicFlightCost = CurrentFlightCost

  # print("FinalBasicFlightCost = ", FinalBasicFlightCost)
  return FinalBasicFlightCost

#===============

def totalFlightCost():
  FlightSpec = input("Please enter your specfication? ")
  result = isFirstClass(FlightSpec) + getChosenMeal(FlightSpec) + getCurrentFlightCost(FlightSpec) + bagCost(FlightSpec) 
  return result
#===============




getFinalBasicFlightCost("AMS 0 11 S F")


