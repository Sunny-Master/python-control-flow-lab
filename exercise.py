# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

#####################################################################################
# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Enter a letter (a-z or A-Z): ')
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if len(letter) > 1 :
        print('Inappropriate input!! You have entered more than 1 character!')
    elif letter.lower() in 'aeiou' :
        print(f'The letter {letter} is a vowel.')
    elif letter.lower() in consonants : 
        print(f'The letter {letter} is a consonant.')
    else :
        print('Inappropriate input!! You didn\'t enter a letter!')

# Call the function
check_letter()

#####################################################################################
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    age = input('Enter your age in number of yrs: ')
    while (not age.isnumeric()) or (int(age) < 0) :
      age = input('Inappropriate input!! Please make sure to enter your age in number of yrs: ')
    if int(age) >= voting_age :
        print('You are eligible to exercise your right to vote!')
    else :
        print('You are not eligible to vote')

# Call the function
check_voting_eligibility()

#####################################################################################
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input('Enter a dog\'s age: ')
    while not dog_age.isnumeric() :
        dog_age = input('Inappropriate input!! Pls correctly enter dog\'s age in number of yrs: ')
    if int(dog_age) <= 2 :
        dog_years = int(dog_age) * 10
    else :
        dog_years = 20 + (int(dog_age)-2) * 7
    print(f'The dog\'s age in dog years is {dog_years}.')

# Call the function
calculate_dog_years()

#####################################################################################
# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = True if input('Is it cold outside? (yes/no): ') == 'yes' else False    
    raining = True if input('Is it raining outside? (yes/no): ') == 'yes' else False
    
    if (cold and raining) :
        print('Wear a waterproof coat.')
    elif (cold and not raining) :
        print('Wear a warm coat.')
    elif (not cold and raining) :
        print('Carry an umbrella')
    else :
        print('Wear light clothing.')

# Call the function
weather_advice()

#####################################################################################
# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    MONTHS = {'jan': 31, 
              'feb': 29, 
              'mar': 31,
              'apr': 30,
              'may': 31,
              'jun': 30,
              'jul': 31,
              'aug': 31,
              'sep': 30,
              'oct': 31,
              'nov': 30,
              'dec': 31
            }
    
    month = input('Enter the month of the year (Jan - Dec): ')
    while month.lower() not in MONTHS :
        month = input('Inappropriate input! Pls enter the month (as three characters)(Jan - Dec): ')
    
    date = input(f'Enter the day of the {month} month: ')
    while not date.isnumeric() and int(date) > MONTHS[month] :
        date = input(f'Inappropriate input! Pls enter the day of the {month} month: ')
    
    mon = month.lower()
    dt = int(date)

    if mon == 'dec':
        season = 'Fall' if dt <= 20 else 'Winter'
    elif mon in ('jan', 'feb') :
        season = 'Winter'
    elif mon == 'mar' :
        season = 'Winter' if dt <= 19 else 'Spring'
    elif mon in ('apr', 'may') :
        season = 'Spring'
    elif mon == 'jun' :
        season = 'Spring' if dt <= 20 else 'Summer'
    elif mon in ('jul', 'aug') :
        season = 'Summer'
    elif mon == 'sep' :
        season = 'Summer' if dt <= 21 else 'Fall'
    else :
        season = 'Fall'      
    
    print(f'{month} {date} is in {season}.')

# Call the function
determine_season()

#####################################################################################
# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    NUMBER = 42
    print('Guess a number in 5 tries between 1 and 99!!')
    for i in range(5) :
        if i == 4 :
            guessed_number = input(f'Last chance! Guess #{i + 1}: ')
        else :
            guessed_number = input(f'Guess #{i + 1}: ')
        if not guessed_number.isnumeric():
            if i == 4 :
              print('Sorry, you failed to guess the number in five attempts.')
            else :
              print(f'{guessed_number} is not a valid input.')
        elif int(guessed_number) == NUMBER :
            print(f'Congratulations, you guessed correctly!! It is indeed {NUMBER}')
            break
        elif i == 4 and int(guessed_number) != NUMBER :
            print('Sorry, you failed to guess the number in five attempts.')
        elif int(guessed_number) > NUMBER :
            print('Guess is too high.')
        else :
            print('Guess is too low.')        
            
# Call the function
guess_number()

