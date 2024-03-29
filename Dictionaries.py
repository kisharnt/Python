# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 11:50:14 2021

@author: kisha
"""
# Capitals = {'France':'Paris','Malaysia':'Kuala Lumpur','Azerbaijan':'Baku', }

# print(Capitals.get('France'))

# capitals['South Korea'] = 'Seoul'
# Capitals('France')

# print(Capitals.items())

# for country,city in Capitals.items():
#     print (f'The capital of {country} is {city}')

# print (7 in Capitals)

'''sherlock = 
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table. I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. It was a fine, thick piece of wood, bulbous-headed, of the sort which is known as a “Penang lawyer.” Just under the head was a broad silver band nearly an inch across. “To James Mortimer, M.R.C.S., from his friends of the C.C.H.,” was engraved upon it, with the date “1884.” It was just such a stick as the old-fashioned family practitioner used to carry—dignified, solid, and reassuring.

“Well, Watson, what do you make of it?”

Holmes was sitting with his back to me, and I had given him no sign of my occupation.

“How did you know what I was doing? I believe you have eyes in the back of your head.”

“I have, at least, a well-polished, silver-plated coffee-pot in front of me,” said he. “But, tell me, Watson, what do you make of our visitor’s stick? Since we have been so unfortunate as to miss him and have no notion of his errand, this accidental souvenir becomes of importance. Let me hear you reconstruct the man by an examination of it.”

“I think,” said I, following as far as I could the methods of my companion, “that Dr. Mortimer is a successful, elderly medical man, well-esteemed since those who know him give him this mark of their appreciation.”

“Good!” said Holmes. “Excellent!”

“I think also that the probability is in favour of his being a country practitioner who does a great deal of his visiting on foot.”

“Why so?”

“Because this stick, though originally a very handsome one has been so knocked about that I can hardly imagine a town practitioner carrying it. The thick-iron ferrule is worn down, so it is evident that he has done a great amount of walking with it.”

“Perfectly sound!” said Holmes.

“And then again, there is the ‘friends of the C.C.H.’ I should guess that to be the Something Hunt, the local hunt to whose members he has possibly given some surgical assistance, and which has made him a small presentation in return.”

“Really, Watson, you excel yourself,” said Holmes, pushing back his chair and lighting a cigarette. “I am bound to say that in all the accounts which you have been so good as to give of my own small achievements you have habitually underrated your own abilities. It may be that you are not yourself luminous, but you are a conductor of light. Some people without possessing genius have a remarkable power of stimulating it. I confess, my dear fellow, that I am very much in your debt.”

He had never said as much before, and I must admit that his words gave me keen pleasure, for I had often been piqued by his indifference to my admiration and to the attempts which I had made to give publicity to his methods. I was proud, too, to think that I had so far mastered his system as to apply it in a way which earned his approval. He now took the stick from my hands and examined it for a few minutes with his naked eyes. Then with an expression of interest he laid down his cigarette, and carrying the cane to the window, he looked over it again with a convex lens.
'''


'''word count'''
# counts = {}
# words = sherlock.split()

# for i in words:
    
##    IDIOM
#     counts[i] = counts.get(i,0) + 1
    
# print('Counts:',counts)

# letter_count = {}
# for letter in sherlock:
#     letter_count[letter.lower()] = letter_count.get(letter,0)+1
    
# #
# #
# ##    
# print(letter_count)    
##    
#import matplotlib.pyplot as plt
##
#
#
#x,y = zip(*letter_count.items())
##
#plt.bar(x,y)
#plt.show()
##
# letter_count_clean = {}

# for k,v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k] = v
        
# print(letter_count_clean)     
#
#x,y = zip(*letter_count_clean.items())
#
#plt.bar(x,y) 
#plt.show()   
#
#
#
# my_list_1 = [1,2,3,4]
# my_list_2 = ['a','b','c','d']

# joined = list(zip(my_list_1,my_list_2))
# print(f'The result of the zip function is {joined} it is of type {type(joined)}')

# i,j = zip(*joined)

#print(capitals.items())
#print()
#x,y = zip(*capitals.items())


#new_words = sherlock.split(' ')
#
#print(new_words)
#
#'Sherlock' in new_words

#for i in range(len(new_words)):
#    new_words[i] = new_words[i].strip('\n')
##    
#print(new_words)

### Tuples

#my_tuple = (1,2,3,4)
#my_list = [5,6,7,8]
#my_string = 'Australia'
#
#my_tuple[0]
#my_tuple[:3]
#
#my_list[0] = 1000
#my_tuple[0] = 2000
#my_string[4] = 'q'
#
### Summary
#
## Lists are mutable
## Dictionaries are mutable
## Tuples are immutable
## Strings are immutable


### Another Dimension

#my_list = [[1,2,3],[4,5,6],[7,8,9]]

#my_list[0]
#my_list[1]
#my_list[2]
#
#my_list[1][1]


#countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
#             'United Kingdom':{'Capital':'London','Language':'English'},
#            'United States':{'Capital':'Washington DC','Language':'English'},
#            'Italy':{'Capital':'Rome','Language':'Italian'}
#            }
##
##
##countries['France']
##
#for key, value in countries.items():
#    print(key,value) 
#
#print()
#for key, value in countries.items():
#    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}.')


# from collections import Counter

# print(Counter(sherlock.lower()))

# new_dict = dict(Counter(sherlock.lower()))
# #
# new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}
# #
# print(new_dict)

# L = [x**2 for x in range(1,11)]

# M = []
# for x in range(1,11):
#     M.append(x**2)

#####

'''PY4E'''
''' Generate word histogram and find the most common word'''

# user_input = input('Please enter a file name:')
# file= open(user_input, encoding="utf8")

# count = {}
# for line in file:
#     line = line.rstrip()
#     line = line.split()
#     for w in line:
#         count[w] = count.get(w,0) + 1
        
# #print(count)

# largest = -1
# biggest = None
# for k,v in count.items():
#     print(k,v)
#     if v is None or v > largest:
#         largest = v
#         biggest = k 

# print (f'The most common word is {biggest} which appears {largest} times')


''''
Write a program to read through the mbox-short.txt and figure out who has 
sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. The 
program creates a Python dictionary that maps the sender's mail address to a 
count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to 
find the most prolific committer.
'''

# user_input = input('Please enter a file name:')
# file= open(user_input, encoding="utf8")

# emailcount = dict()
# for line in file:
#     if not line.startswith("From: "):
#         continue
#     line = line.rstrip()
#     line = line.split()
#     line = line[1]
#     emailcount[line] = emailcount.get(line,0) + 1

# bigword = None
# bigcount = None
# for email, value in emailcount.items():
#     if bigcount is None or value > bigcount:
#         bigcount = value
#         bigword = email

# print(f'The most common email is {bigword} which appears {bigcount} times')

''' Tuples
Sort word count by descending order
'''

# user_input = input('Please enter a file name:')
# file= open(user_input, encoding="utf8")

# count = {}
# for line in file:
#     line = line.rstrip()
#     line = line.split()
#     for w in line:
#         count[w] = count.get(w,0) + 1

# tmp = []
# for k,v in count.items():
#     newt = v,k
#     tmp.append(newt)
    
# tmp = sorted(tmp,reverse=True)

# for v,k in tmp[:5]:
#     print(k,v)

'''
10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the 
hour out from the 'From ' line by finding the time and then splitting the 
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

# user_input = input('Please enter a file name:')
# file= open(user_input, encoding="utf8")

# email = dict()
# for line in file:
#     if not line.startswith("From "):
#         continue
#     if line == '':
#         continue
#     words = line.split()
#     time = words[5].split(':') 
#     print(time)
#     hours = time[0]
#     email[hours] = email.get(hours, 0) + 1

# order = list()

# for hours, frequency in email.items():
#     order.append((frequency, hours))

# order = sorted(order, reverse=True)

# for frequency, hours in order:
#     print(hours, frequency)


'''A researcher has gathered thousands of news articles. But she wants to focus 
her attention on articles including a specific word. Complete the function 
below to help her filter her list of articles.

Your function should meet the following criteria:

1. Do not include documents where the keyword string shows up only as a part of a 
larger word. For example, if she were looking for the keyword “closed”, you 
would not include the string “enclosed.”
2. She does not want you to distinguish upper case from lower case letters. So the 
phrase “Close   d the case.” would be included when the keyword is “closed”
3. Do not let periods or commas affect what is matched. “It is closed.” would be
included when the keyword is “closed”. But you can assume there are no other 
types of punctuation.
'''
'''Solution 1'''
def word_search(doc_list, keyword):
    indices = []
    keyword = keyword.lower()
    for counter, doc in enumerate(doc_list):
        doc = doc.lower()
        doc = doc.replace(".","")
        doc = doc.replace(",","")
        doc_words = doc.split()
        if keyword in doc_words:
            indices.append(counter)
    return indices

'''Solution 2'''
    
def word_search(doc_list, keyword):
    indices = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens] #list comprehension
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


''' Returns multiple keywords'''

def multi_word_search(doc_list, keywords):
    
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices


x = multi_word_search(["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"], ['casino', 'they'])
print(x)
















