class User: #creating a class
    def __init__(self, user_id, user_name):
        #create the starting values for the attributes
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Lauren") #initialize an object from our class (blueprint) called User
user2 = User("002", "Jack")

print(user1.id)

#Creating Attributes for the object (variables associated with an object)
user1.id = "001"
user1.username = "Lauren"

#Methods are the things that the object does (functions within the object)

user1.follow(user2)
print(user1.followers)
print(user1.following)

