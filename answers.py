
#question1 Write a Python script to add a key-value pair to a dictionary
mydict = {0:10, 1:20}
key = int(input())
value = int(input())
mydict[key] = value
mydict[2] = 20
print(mydict)

#question2 Write a Python program to iterate over dictionaries using for loops
mydict = {0: 10, 1: 20, 2:30, 3:40}
def ite(mydict):
    for key in mydict:
        #result = mydict[key]
        #print(result)
        print(mydict[key])
    #return None
var = ite(mydict)
print(var)
#print(ite(mydict))



#question3 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
mydict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
for k in mydict:
    if 1 >= k >= 15:
        print(k, mydict[k])
    if mydict[k] ==  k * k:
        print(k, mydict[k])

#question4 Write a Python function to find the Max of three numbers **Hint: Use return, loop and if** (but the answer prints the max 1 not 3 numbers?)
lst = [6,2,8]
def MaxThree(lst):
    if len(lst) == 0:
        return None
    mymax =lst[0]
    for i in lst:
        if i > mymax:
            mymax = i
    return mymax
mymax = MaxThree(lst)
print(mymax)

#question4 alternative answer
lst = [6,2,8]
def AltMAxThree(lst):
    for i in lst:
        if i == max(lst):
         return i
mymax = AltMAxThree(lst)
print(mymax)


#question5 Write a Python function to multiply all the numbers in a list.
lst = [1,3,5,7,9]
def MultiplyALL(lst):
    result = 1
    for i in lst:
        result = result * i
    return (result)
product = MultiplyALL(lst)
print(product)
