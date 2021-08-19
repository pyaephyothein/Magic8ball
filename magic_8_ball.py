user_input_name = input("Enter Your Name :")
user_input_question = input("Enter Your Question :")
answer = ()
import random
random_number = random.randint(1,12)
if random_number == 1:
    answer = "Yes - definitely"
elif random_number ==2:
    answer = "It is decidedly so"
elif random_number ==3:
    answer = "Reply hazy, try again"
elif random_number == 4:
    answer = "Ask again later"
elif random_number == 5:
    answer = "Better not tell you now"
elif random_number == 6:
    answer = "My sources say no"
elif random_number == 7:
    answer = "Outlook not so good"
elif random_number == 8:
    answer = "Very doubtful"
elif random_number == 9:
    answer = "Without a doubt"
elif random_number == 10:
    answer = "GG man"
elif random_number == 11:
    answer = "May Be"
elif random_number == 12:
    answer = "Absolutely Sure "
else:
    answer = "Error"
print(user_input_name + " asks : " + user_input_question)
print("Magic8 balls answer is : " + answer)