#q1
def Describe_Stats(nbr_list):
    result = {}  #define empty dict
    result['sum']=sum(nbr_list)
    result['max']=max(nbr_list)
    result['min']=min(nbr_list)
    result['mean']=result['sum']/len(nbr_list)

    return result

#q2
def Common_Data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                #once we find a common element, we can exit the function
                return result 
    return result

#q3
#check out https://thispointer.com/how-to-merge-two-or-more-dictionaries-in-python/
def Combine_Dict(dict1,dict2):
    result = {} #define empty dict
    #google search on how to iterate through dict, key value pairs
    #for key in dict1.keys() also works
    #this function assumes both dict1 and dict2 have the same keys
    for key, value in dict1.items():
        result[key] = dict1[key]+dict2[key]
    
    return result

def Combine_Dict2(dict1,dict2):
    #alternate solution
    from collections import Counter
    result = Counter(dict1) + Counter(dict2)
    return result



#q4
def FizzBuzz(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz") #if divisible by 3 and 5
            continue #continue out of the for loop
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("buzz")
            continue
        print(i)
	

#q5
def Check_Password(p):
    import re
    x = True
    while x:
        if (len(p)<6 or len(p)>16):
            break #break out of while loop
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[0-9]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif re.search("\s",p): #this is whitespace character
            break
        else:
            print("Valid Password")
            x=False
            break

    if x:
        print("Not a Valid Password")


#alternative solution 
def Check_Password2(p):
    import string
    small_ltr = set(string.ascii_lowercase)
    #defining it yourself is one way but not advisable
    #google search how to get small letter alphabets in python
    #small_ltr = set(['a','b',....]) 
    capital_ltr = set(string.ascii_uppercase)
    nbrs= set(string.digits)  #from 0-9
    special_char = set(['$','#','@'])

    #same logic as Check_Password1
    #this is one way of doing it, not the only way
    x=True
    while x:
        if (len(p)<6 or len(p)>16):
            break #break out of while loop
        elif len(set(p).intersection(small_ltr))== 0:
            #if they have no common elements
            break
        elif len(set(p).intersection(capital_ltr))== 0:
            break
        elif len(set(p).intersection(nbrs))== 0:
            break
        elif len(set(p).intersection(special_char))== 0:
            break
        elif "\s" in p:
            break
        else:
            print("Valid Password")
            x=False
            break

    if x:
        print("Not a Valid Password")


#Q6
def Unique_Elt(list1):
    #transform a list into a set then transform back into list
    return list(set(list1))

#Q7
def Hypotenuse_Length(height,base):
    #google search how to square root
    import math
    return math.sqrt(height*height + base*base)


#Q8
def Scrable_Score(word):
    POINTS = dict([(x, 1) for x in 'AEIOULNRST'] +
    [(x, 2) for x in 'DG'] +
    [(x, 3) for x in 'BCMP'] +
    [(x, 4) for x in 'FHVWY'] +
    [(x, 5) for x in 'K'] +
    [(x, 8) for x in 'JX'] + 
    [(x, 10) for x in 'QZ'])

    #or a straight forward way to create a dict
    #POINTS = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    #'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    #'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    #'Y': 4, 'Z': 10}

    if not word.isalpha():
        return 0
    return sum(POINTS[x] for x in word.upper())


#Q9
def gcd(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return gcd(low, high%low)


#test the functions

#1
nbrs = [1,2,3,4,5,6]
stats = Describe_Stats(nbrs)
print(stats)

#2
list1 = ['Tom', 'Bob', 'Sue', 'Rachel']
list2 = ['Bob', 'Susan', 'Roger', 'Mike']
HaveCommonElt = Common_Data(list1, list2)
print(HaveCommonElt)

#3
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'c':400}
d3 = {'a': 300, 'b': 200, 'd':400}
combined_dict = Combine_Dict(d1,d2) #same keys
combined_dict2 = Combine_Dict2(d1,d3) #different keys
print(combined_dict)
print(combined_dict2)

#4
FizzBuzz(100)


#5
Check_Password('Password1990$')
Check_Password2('Password1990$')
Check_Password('password199')

#6
print(Unique_Elt([1,2,3,3,3,3,4,4,5]))

#7
hypotenuse = Hypotenuse_Length(3,4)
print(hypotenuse)

#8
print(Scrable_Score('cabbage'))

#9
res = gcd(45,120)
print(res)