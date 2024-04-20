# Activity Python 1: Task 2
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 30 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

import math, random

team = open('TeamQuestion.txt' , 'r')
new_q = open('QuestionsToAsk.txt', 'w')


NumberOfLines = (team.readlines())

questions = int(input('How many questions to store in new file? '))
original = 0

    
while original < questions:
    LineSelect = random.randint(0,len(NumberOfLines) - 1)
    print(NumberOfLines[LineSelect])
    
    userAsk = str(input('Would you like to keep this question? [y or n]'))
    
    if userAsk == "y":
        original = original + 1
        new_q.write(NumberOfLines[LineSelect])
    elif userAsk == "n":
        pass
    else:
        print("error")

new_q.close()
team.close()