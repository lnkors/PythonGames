print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("$5.")
        bill = 5
    elif age <= 18:
        print("$7.")
        bill = 7
    else:
        print("$12.")
        bill = 12

    want_photo = input("Do you want a photo? Type Y for Yes and N for No")
    if want_photo == "Y":
        bill += 3

    print(f"Your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
