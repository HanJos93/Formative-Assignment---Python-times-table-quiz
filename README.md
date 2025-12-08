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
The above code manages the introduction to the quiz, once any character is entered it begins a 3 second countdown using a 'for i in range' loop that waits 1 second using time.sleep before subtracting 1 from the variable and printing each step of the countdown.
