import game_data
import art
import random

data = game_data.data

def random_generator():
    l = len(data)
    num = random.randint(0, l)
    person = data[num]["name"]
    descp = data[num]["description"]
    place = data[num]["country"]
    followers = data[num]["follower_count"]
    st = f"{person}, {descp}, {place}"
    return st, followers

def higher_lower_game():
    score = 0
    is_playing = True
    a_compare, followers1 = random_generator()

    while is_playing:

        print(art.logo)
        print(f"Compare A: {a_compare}")

        print(art.vs)

        b_compare, followers2 = random_generator()
        print(f"Compare B: {b_compare}")

        answer = input("Who has more followers? Type A or B: ")
        if followers1 > followers2 and answer == 'A':
            score += 1
            print(f"You're right! Current score: {score}")
            a_compare = b_compare
            followers2 = followers1
        elif followers1 > followers2 and answer =="B":
            print(f"Sorry, you're wrong. Final score: {score} ")
            is_playing = False
        elif followers1 < followers2 and answer == "A":
            print(f"Sorry, you're wrong. Final score: {score} ")
            is_playing = False
        else:
            score += 1
            print(f"You're right! Current score: {score}")
            a_compare = b_compare
            followers2 = followers1

higher_lower_game()