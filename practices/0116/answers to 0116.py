
#1. Write a function to find min value of a list
def find_min(lst):
    if len(lst) == 0:
        return None
    min_value =lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value
    return None

lst = [1,5,2,9,28,32,13]
result = find_min(lst)
print('Min value is '+ str(result))

# 2. Remove duplicates from a list
# Write a Python function that takes a list and returns a new list with unique elements of the first list


#answer1:
def remove_dup(lst):
    # create new list
    newlst = []
    # iterate through lst
    for i in lst:
        #print(i)
        #print(newlst)
        # if element already exists in the new list
        if i in newlst:
            # branch A
            # don't do anything
            continue
        # if element doesn't exists in the new list
        else:
            # branch B
            # then add it to our new list
            newlst.append(i)
    # return new list
    return newlst

lst = [1,1,3,3,2,2,5,5,13,28]
result = remove_dup(lst)
print(result)



answer2:
# def remove_dup(lst):
#     # Add content here
#     return
import numpy as np
lst = [1,1,3,3,2,2,5,5,13,28]
result = np.unique(lst)
#result = remove_dup(lst)
print(result)



#3. Calculate the number of uppercase letters and lowercase letters
#Write a Python function that accepts a string and calculate the number of uppercase letters and lower case letters

answer1:
def cal_cases(mystr):
    num_upper = sum(1 for c in mystr if c.isupper())
    num_lower = sum(1 for c in mystr if c.islower())
    # Add content here
    return [num_upper, num_lower]

test_str = 'This is My houSE.'
result = cal_cases(test_str)
print(result)

answer2:
def cal_cases(mystr):

    num_upper = 0
    num_lower = 0
    for c in mystr:
        if c.isupper():
            num_upper += 1
        if c.islower():
            num_lower += 1

    return [num_upper, num_lower]

test_str = 'This is My houSE.'
result = cal_cases(test_str)
print(result)


# 4. Reverse a String
# Write a function to reverse a string
answer1:
def str_rev(mystr):
   result = mystr[::-1]
   return result

test_str = 'HelloWorld'
result = str_rev(test_str)
print(result)

answer2:
def str_rev(mystr):
   #result = mystr[::-1]
   result = ''
   for i in mystr:
       result = i + result

   return result

mytest_str = 'HelloWorld'
result = str_rev(mytest_str)
print(result)
