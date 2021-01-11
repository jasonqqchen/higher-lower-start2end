from art import logo, vs
from game_data import data 
import random
#1. select two random questions from the 50 database. 
is_game_over = False
user_score = 0

while not is_game_over:
    question1 = data[random.randrange(0,49)]
    question2 = data[random.randrange(0,49)]
    #1.5 get the data from this question
    def get_data(question):
        key_list = []
        value_list = []
        for key in question:
            key_list.append(key)
            value_list.append(question[key])
        return key_list,value_list

    data1 = get_data(question1)
    data2 = get_data(question2)


    q1_answer = question1['follower_count']
    q2_answer = question2['follower_count']
    # print(q1_answer)
    # print(q2_answer)

    game_answer = ''
    if q1_answer > q2_answer:
        game_answer = 'A'
    else:
        game_answer = 'B'
    #2. Show the questions, Ask user to guess which one is higher
    print(logo)
    print(f"Compare A: {data1[1][3]}, {data1[1][2]}, {data1[1][0]}")
    print(vs)
    print(f"Compare B: {data2[1][3]}, {data2[1][2]}, {data2[1][0]}")

    user_guess = input("who has more follower 'A' or'B'? ")
    #3. If the user win the game,added one
    if user_guess == game_answer:
        print("you win the game, next question is")
        user_score += 1
    else:
        print(f"lose the game, your score is {user_score} ")
        is_game_over = True
#4. If the user lose the game, show the final result
#5. format is same so we can asked the question with the same format. 






