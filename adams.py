'''
#pallindrome
num=int(input("enter a value:"))
value=num
a=0
while num>0:
    a=(a*10)+num%10
    num//=10
print(a)
if(value==a):
    print("value is equal to num")
    print("a is pallindrome")
else:
    print("is not pallindrome")


#string pallindrome
a=str('madam')
a==a[::-1]
print(a)

 #Armstrong number


num=153
a=0
value=num
while value>0:
    r=value%10
    a=a+r**3
    value//=10

if num==a:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")



'''

#Adam number
def reversedigit(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num//=10
    return rev

def square(num):
    return(num*num)
def checkadamnumber(num):
    a=square(num)
    b=square(reversedigit(num))
    if(b==reversedigit(a)):
       return True
    else:
       return False    

num=12
if(checkadamnumber(num)):
    print("adam number")
else:
    print("not a adam number")



    
