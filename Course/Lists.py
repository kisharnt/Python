# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:52:12 2021

@author: kisha
"""

'''
Open the file romeo.txt and read it line by line. For each line, 
plit the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line
check to see if the word is already in the list and if not append it to 
the list. When the program completes, sort and print the resulting words
in alphabetical order.You can download the sample data at 
http://www.py4e.com/code3/romeo.txt
'''


file = input('Please input file name:')
file_name= open(file)
store = []

for line in file_name:
    line = line.split()
    for char in line:
        if char in store:
            continue
        else: 
            store.append(char)

print(store)



'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a 
line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word 
in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print 
the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

# file = input('Please input file name:')
# file_name= open(file)
# count =[]

# for line in file_name:
#     line = line.rstrip()
#     words = line.split()
    
#     # Guardian pattern 
#     if len(words)<3:
#         continue
#     if words[0] != 'From':
#         continue
#     count.append(words[1])

# print(f'There were {len(count)} lines in the file')