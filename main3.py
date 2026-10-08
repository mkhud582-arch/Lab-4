from classes import Team, Driver

# your code herewrite code that reads this data and creates 
# a Team object for each team, a Driver object for each driver, and adds each 
# Driver object to the appropriate Team. Store the team objects in a collection
#  of some kind.
#When you're finished, the collection should contain 10 Team objects,
#each with 2 or more Driver objects. Note that each team appears multiple times in
#the dataset: be careful to create only one Team object for each team.
teams = {}
with open('f1_point.txt', 'r') as file:
    next(file)  # Skip the header
    for line in file:
        driver_name, team_name, points = line.strip().split(',')
        points = int(points)

        # Create or retrieve the team
        if team_name not in teams:
            teams[team_name] = Team(team_name)

        # Create the driver and add them to the team
        driver = Driver(driver_name, points)
        teams[team_name].add_driver(driver)