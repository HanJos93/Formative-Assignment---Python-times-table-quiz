#Imports random library
import random

#Imports time library
import time

#Introduction to the quiz
quiz_intro = str(input("Welcome to my times-table quiz! You will have 60 seconds to get as many answers correct as possible. Type anything to begin "))
qcountdown = 4
#Start a 3 second countdown for the quiz
for i in range(qcountdown):
    time.sleep(1)
    qcountdown = qcountdown - 1
    print (f"{qcountdown} !")
    if qcountdown == 1:
        print ("Begin!")
        break


#Variable to keep track of score
score = 0

#Question generator and countdown
qtimelimit = (60) #Sets the time limit (in seconds) for the quiz
qtimerstart = time.time() #Records current time since epoch in seconds
for i in range (qtimelimit):
    num1 = random.randint(1, 12) #Defines the first number
    num2 = random.randint(1, 12) #Defines the second number
    answer = int(num1*num2) #Defines the answer
    question = int(input(f"{num1} * {num2} " )) #Generates a question that times num1 by num2
    if question == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
    qtimercheck = time.time() #Records current time since epoch in seconds
    qtimerend = qtimercheck - qtimerstart #Subtracts start time from current time
    if qtimerend >=qtimelimit: #If current time is equal to or greater than the limit, the quiz ends
        print (f"Time is up! You scored {score}. Try again for a better score!")
        break

