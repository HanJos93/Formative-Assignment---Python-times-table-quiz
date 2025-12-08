# Python-times-table-quiz
## User Guide
### Step 1: Download the Python script
Download Timestablequiz.py
### Step 2: Open Timestablequiz.py
Open with your preferred environment, it can be run directly from the Python terminal
### Step 3: Start the quiz
Once the code is run, you will be able to start the quiz by entering any character and clicking enter. This will start a 3 second countdown before the quiz begins.
### Python libraries
This script uses random and time, ensure these are installed.
## Technical documentation
You can edit the code by opening the .py file in your preferred environment. The script was created and run entirely within Visual Studio Code.
```python
quiz_intro = str(input("Welcome to my times-table quiz! You will have 60 seconds to get as many answers correct as possible. Type anything to begin "))
qcountdown = 4
for i in range(qcountdown):
    time.sleep(1)
    qcountdown = qcountdown - 1
    print (f"{qcountdown} !")
    if qcountdown == 1:
        print ("Begin!")
        break
```
quiz_intro is a user input which asks for the user to enter any character to begin the quiz.
qcountdown is a variable used as a countdown. Once run each second using time.sleep the variable will subtract 1 until it reaches 1, each second of the countdown it will print the current value.

```python
qtimelimit = (60)
qtimerstart = time.time() 
```
The qtimelimit variable is used to set how long (in seconds) the quiz lasts, editting this variable alone will allow you to customise the time limit for the quiz. 
Qtimerstart records the current time in seconds since epoch and will be used to calculate how long is left in the quiz after each answered question.

```python
for i in range (qtimelimit):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = int(num1*num2) 
    question = int(input(f"{num1} * {num2} " ))
```
The 'for i in range' loop allows the following questions to loop for as long as the time limit set in qtimelimit is not exceeded. 
The num1 and num2 variables are assigned random values from a range of 1 to 12 each loop using the randint function from the random library. You can adjust the values to customise the questions you will be asked. 
The answer varaible multiplies num1 and num2 to define what the answer should be
The question variable outputs a times-table question using the values assigned to num1 and num2.

```python
if question == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")
```
If the user input in the variable question is the same as answer, the question is considered correct and a value of +1 is added to the score and a new question is generated. If it does not match, no value is added to the score and a new question is generated.
