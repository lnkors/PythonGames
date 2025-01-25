states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York",
                     "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
                     "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
                     "Hawaii"]
#Use square brackets always with lists (indexing and creating lists)
print(states_of_america[-1]) #First index is zero! Last index is -1

states_of_america[1] = ("Lauren") #Editing an Index
print(states_of_america)

states_of_america.append("Korsnick_Land") #Adds one item to the end of the list
print(states_of_america)

states_of_america.extend(["Korsnick_Land", "Jonland", "Ryanland"])
print(states_of_america)