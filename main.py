

#===============

def bagCost(numOfBags):
  bagCost = 0
  if numOfBags <= 1:
    bagCost = bagCost
    print(bagCost)
  else:
    bagCost = (numOfBags - 1) * 20
    print(bagCost)
    
  return bagCost

#================

def getCurrentFlightCost(passAge, destination):
  BasicFlightCostAMS = 150
  BasicFlightCostGLA = 80
  CurrentFlightCost = 0

  if destination == "GLA":
    if passAge <= 15:
      CurrentFlightCost = BasicFlightCostGLA / 2
      print(CurrentFlightCost)
    else:
      CurrentFlightCost = BasicFlightCostGLA
      print(CurrentFlightCost)
      

  if destination == "AMS":
    if passAge <= 15:
      CurrentFlightCost = BasicFlightCostAMS / 2
    else:
      CurrentFlightCost = BasicFlightCostAMS
    
  return CurrentFlightCost

#===============

def getChosenMeal(passAge, MealChosen):
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

def isFirstClass(CurrentFlightCost, SeatType):
  FinalBasicFlightCost = 0

  if SeatType == "F":
    FinalBasicFlightCost = CurrentFlightCost * 6
  else:
    FinalBasicFlightCost = CurrentFlightCost

  print("FinalBasicFlightCost = ", FinalBasicFlightCost)
  return FinalBasicFlightCost

#===============

getChosenMeal(1, "S")
isFirstClass(80, "F")
getCurrentFlightCost(1, "GLA")
bagCost(0)





