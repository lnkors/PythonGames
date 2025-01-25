enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope exists within functions
#cannot call variable within the functions
#globa variables are avalible within functions, be aware where you create varibles and create a namespace
