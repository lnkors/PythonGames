import turtle

#We can construct our object from that blueprint
#timmy = turtle.Turtle() #created an object using an imported module
#print(timmy)
#changing different attributes of timmy
#timmy.shape("turtle")
#timmy.color("cyan")
#timmy.forward(100)

#my_screen = turtle.Screen()
#Atrributes that the object Screen has
#print(my_screen.canvheight)

#call a function associated with an object
#my_screen.exitonclick()

#From this blueprint prettytable which we downloaded on python we are importing the class PrettyTable
#From a class you can create different objects

from prettytable import PrettyTable

#From that class, we are creating an object called table
table = PrettyTable()

#Now we can use the functionality of the object which has the functionality to add columns
#Functions (Method)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Change the attributes of the table
#Field
table.align = "r"

print(table)