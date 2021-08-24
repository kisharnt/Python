# hours = float(input('Please enter the number of hours you worked this week:'))
# rate_per_hour = float(input('Please enter the rate per hour as per your contract:'))

# if not(hours.is_integer() and rate_per_hour.is_integer()):
#     print('Please enter a correct value')
# else:
#     print('Let us calculate your pay:')

# def computepay(x, y):
#     if x<40:
#         return x*y
#     else:
#         return (x*y) + ((x-40)*(y*0.5))

# final_pay = computepay(hours,rate_per_hour)
# print('Pay',final_pay)

# f = open('kipling.txt','w')

'''Fibonacci Function'''

# def fib(n):
#     '''Calculate and returns the nth fibonacci number'''
#     a = 0
#     b = 1
#     for i in range(n):
#         a,b = b,a+b
        
#     return a

'''More functions'''

#def sum_and_mult(a,b):
#    total = a + b
#    product = a * b
#    
#    return total, product
##
#func_call = sum_and_mult(3,4)
##
#print(func_call)
#print(type(func_call))
##
#var_1, var_2 = sum_and_mult(6,7)
##
##
##
#var_3 = 5
#var_4 = 6
##
#def add1(var_3,var_4):
#    var_3 = var_3 + 1
#    var_4 = var_4 + 1
#    
#    print(f'Inside the function var_3 = {var_3} and var_4 = {var_4}')
#    return var_3,var_4
##
#add1(18,19)
#
#print(f'But outside the function var_3 = {var_3} and var_4 = {var_4}')


#def lengthen_list(n,my_list = [1,2,3]):
#    my_list.append(n)
#    
#    return my_list
#
#x = lengthen_list(4)
#
#x = lengthen_list(4)
##
#x = lengthen_list(4)
##
#def lengthen_list_2(n,my_list = None):
#    if my_list == None:
#        my_list = [1,2,3]
#        my_list.append(n)
#        return my_list
#    
#y = lengthen_list_2(4)
##
#y = lengthen_list_2(4)
##
#y = lengthen_list_2(4)

    
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


party_attendees = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
x = fashionably_late(party_attendees,'Saturn')
print(x)



