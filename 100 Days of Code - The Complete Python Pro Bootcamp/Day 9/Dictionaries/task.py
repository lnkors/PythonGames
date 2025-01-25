#Ensure the key is the same data type as you are indexing
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"]) #You get something out of a dictionary using the key

#Add data into the dictionary
programming_dictionary["Loop2"] = "Another loop"
print(programming_dictionary)

empty_lift = []
empty_dictionary = {} #empty dicitonary usage

#Edit an item that already exists in here (same syntax as adding, but will look for the key)
programming_dictionary["Bug"] = "Write something else here"

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])