## This function checks if the specification follows the rules given.


def specChecker(flightSpec):
  
  # Check if the length of the spec is less than 12 chars
  if len(flightSpec) < 12:
    return ("Incorrect specification length, restart program and enter again.")
  else:
    print("Valid Spec length")

  # Check if an appropriate destination has been chosen.
  if destination != "GLA" or destination != "AMS":
    return ("The destination you have entered is invalid, restart program and enter again.")
  else:
    print("Valid destination entered")

  # Check if the age entered is appropriate.
  if passAge <= 0 or passAge > 99:
    return ("The age is invalid, restart program and enter again.")
  else:
    print("Valid age entered")

  # Check if the meal entered is valid.
  if MealChosen != "S" or MealChosen != "V" or MealChosen != "N":
    return ("Enter a valid meal type, restart program and enter again.")
  else:
    print("Valid meal type entered")