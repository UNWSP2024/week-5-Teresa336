# Programmer: Teresa Fischer
# Date: 10/1/24
# Title: Program #2: Math Quiz

# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
#     247
# + 129
# Ask question
print('What is')
print(222, '+', 160, '=')

def add_numbers():
    number1 = 222
    number2 = 160
    answer = number1 + number2
    return answer
# ------

# The program should allow the student to enter the answer.
student_answer = int(input('Enter the answer:'))
# If the answer is correct, a message of congratulations should be displayed.
if student_answer == add_numbers():
    print('Yes! That is correct! Good work!')
# If the answer is incorrect a message showing the correct answer should be displayed.
else:
    print('Sorry, that is incorrect. The correct answer is', add_numbers(), '.')
# The program must use a function that accomplishes part of the needed tasks.