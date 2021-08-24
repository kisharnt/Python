# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:53:18 2021

@author: kisha
"""

#conditional 

# user_input = str(input('Please enter a number between one and two \n'))
# user_input = user_input.lower()

# if user_input == 'one':
#     print ('your number is 1')
# elif user_input =='two':
#     print ('your number is 2')
# else:
#     print ('you are wrong')
    
#example 2
# name = str(input('Please enter your name: \n'))
# name_length = len(name)
# if name_length>5:
#     print('Your name has',name_length,'characters')
# else:
#     print('Your name is a secret')

#example 3

# int_1 = int(input('Please enter a number between 1 and 20:'))
# int_2 = int(input('Please enter another number between 1 and 20:'))
# if int_1>15 and int_2>15:
#     print ('The multiple of your numbers are',int_1*int_2)
# elif int_1>15 or int_2>15:
#     print(int_1+int_2)
# else:
#     print (0)

int_1 = int(input('Please enter a number between 1 and 20:'))
int_2 = int(input('Please enter another number between 1 and 20:'))
int_1, int_2 = int_2, int_1
print(int_1,int_2)








