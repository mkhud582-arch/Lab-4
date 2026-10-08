# Test Cases

from main3 import Driver, Team

# Normal Case

# Normal case

driver1 = Driver("Max Verstappen", 454) # create driver object 
print("Input: Driver('Max Verstappen', 454)")
print("Expected: Driver is created with name Max Verstappen and 454 points")
print("Actual:", driver1)



# Special case: team with no drivers

# The program handles a Team with no drivers


empty_team = Team("Empty Team") # create a Team object with no drivers instead of one or more

print("\nInput: Empty team with no drivers")
print("Expected total points: 0")
print("Actual:", empty_team.get_total_points())

# Error Case 

try:
    bad_line = "Max Verstappen,RED BULL RACING"
    driver_name, team_name, points = bad_line.strip().split(',') # variable mismatch; 3 variables on the left and 2 values on the right

    print("Input:", bad_line)
    print("Expected: Error because the row has the wrong number of values")
    print("Actual: No error occurred")

except ValueError as error_case:
    print("\nInput:", bad_line)
    print("Expected: ValueError because the row has the wrong number of values")
    print("Actual: ValueError detected:", error_case)