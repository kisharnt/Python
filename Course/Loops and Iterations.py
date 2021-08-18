# for i in range (1,10,2):
#     print(i, end=' ')

## for loop for a character 

# word = 'python'
# for char in word:
#     print (char)

## LISTS

# data = [42, 35, 56, 2, 1, 78, 13]
# print(data[0])
# print(data[4])
# print(data[-1])
# print(data[0:4])

# for num in data:
#     print(num)

# for i in range(4):
#     print(data[i])
#     print(data[i+1])
#     print()


# Buble sort ---> can use sorted() function normally, this is just an example 

# data_copy = data[:] 
# #keep original copy safe

# for i in range(len(data_copy)):
#     for j in range(len(data_copy)-i-1):
#         if data_copy[j] > data_copy[j+1]:
#             data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]

# print(data_copy)

''' APPEND/REMOVE '''

# data.append(10000)
# print(data)

# data.remove(78)
# print(data)

## WHILE 

# n = 10
# while n > 0:
#     print (n)
#     n = n-1

# count = 0 
# class_names = []
# name = input('Please enter a student name. Enter \'n\' to stop')
# while name != 'n':
#     count += 1
#     class_names.append(name)
#     print(f'{name} has been added')
#     name = input('Add next name:')

# print(f'There are {count} people in the class and their names are {class_names}')

## RANGE --> Creates an iterator, Creates the numbers as it needs them so very memory efficient 

#print(list(range(10)))


## BREAK and CONTINUE
## TRY and EXCEPT

''' EXCERCISE 1 '''

# while True:
#         num_1 = input('Enter your first number between 1 and 100:')
#         num_2 = input('Enter your second number between 1 and 100:')

#         try:
#             num_1 = int(num_1)
#             num_2 = int(num_2)
#             break
#         except:
#             print('Please enter a number between 1 and 100:')
#             continue

# for i in range(num_1,num_2):
#     print(i,' ')

''' EXCERCISE 2 '''

# while True:
#         num_1 = input('Enter your first number between 1 and 100:')
#         num_2 = input('Enter your second number between 1 and 100:')

#         try:
#             num_1 = int(num_1)
#             num_2 = int(num_2)
#             break
#         except:
#             print('Please enter a number between 1 and 100:')
#             continue

# for i in range(num_1,num_2):
#     print(i,' ')

''' EXCERCISE '''

# word = input('Enter a word, we will reverse it: ')
# print(word[::-1]) 


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

#user_input = input('Please enter a number between 1 and 12:> ')
#
#while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) >12):
#    print('Must be an integer between 1 and 12')
#    user_input = input('Please make selection:> ' )
#user_input = int(user_input)
#print('===============================')
#print()
#print(f'This is the {user_input} times table')
#print()
#for i in range(1,13):
#    print(f'{i} x {user_input} = {i*user_input}')


'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

# for i in range(1,13):
#     print(f'this is the {i} times table')
#     for j in range (1,13):
#         print(f'{i} x {j} = {i*j}')
        
'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

# user_input = input('Please enter a number: ')
# numbers =[]

# while user_input != 'exit':
#     while not user_input.isdigit():
#         print ('That is not a number:')
#         user_input = input('Please enter a number:')
#     numbers.append(int(user_input))
#     user_input = input('Enter another number:')

# total = 0 
# for number in numbers:
#     total = total + number 

# print (f'The mean is {total/len(numbers)}')

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing 
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

### Number of fib numbers required
#n = 20
#
## Set a and b to the first two numbers in the sequence
#a = 0
#b = 1 
#
## List in which to store numbers
#fib_nums = []
#
## Use a for loop to create the sequence, repeat n times
#for i in range(n):
#    fib_nums.append(a)
#    a,b = b,a+b     
#    
#print(f'The first {n} Fibonacci numbers are, {fib_nums}')


'''
Question 9

     *****
     *
     **** 
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

#star = '*'
#
#for i in range(1,7):
#    for j in range(1,6):
#        if i == 1 and j < 6:
#            print(star,end='')
#        elif i == 2 and j == 1:
#            print()
#            print(star)
#        elif i == 3 and j < 5:
#            print(star,end='')
#        elif i == 4 and j == 1:
#            print()
#            print(star)  
#        elif i == 5 and j == 1:
#            print(star)
#        elif i == 6 and j == 1:
#            print(star)    


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

# # Numbers required
# n = 100

# # Instantiate empty lists
# evens = []
# odds = []

# for i in range(n+1):
#     if (i % 2) == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(f'The evens are {evens}')
# print(f'The odds are {odds}')

'''
PY4E Excercise 
Write a program that repeatedly prompts a user for integer numbers 
until the user enters 'done'. Once 'done' is entered, print out the largest and 
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the 
number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''

'''2 METHODS OF SOLVING'''

# user_input = input('Please enter a number, to exit enter done: ')
# nums = []

# while user_input != 'done':
#     while not user_input.isdigit():
#         print ('Invalid Input')
#         user_input = input('Please enter a number: ')
#     nums.append(int(user_input))
#     user_input = input('Enter next number:')
    
# print ('Maximum is', max(nums))
# print ('Minimum is', min(nums))     


# largest = None
# smallest = None
# while True:
#         num = input('Please enter a number: ')
#         if num == 'done':
#             break
#         try: 
#             nums = int(num)    
#         except:
#               print('Invalid input')
#               continue

#         if largest is None or largest < nums:
#             largest = nums
#         if smallest is None or smallest > nums:
#             smallest = nums

# print('Maximum is',largest)
# print('Minimum is',smallest)




