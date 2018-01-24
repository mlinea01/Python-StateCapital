leaveProgram = 0

while leaveProgram != "q":
    state_caps = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
                  'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
                  'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                  'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                  'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
                  'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                  'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
                  'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                  'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                  'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                  'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Lake City',
                  'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'Wisconsin': 'Madison',
                  'Wyoming': 'Cheyenne'
                  }

    for state in state_caps:
        state = input("Enter a state to see it's Capital.(Case Sensitive)")

        if state in state_caps:
            print(state_caps[state])
            break

        else:
            print("Could not find what you are looking for! Check your spelling and trying again!")

    leaveProgram = input("Press enter to continue or q to quit")