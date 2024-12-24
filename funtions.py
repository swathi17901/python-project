
def abc():
    print("name")
    print("place")
    print(123)
abc()
abc()
abc()  
 

def soul(b,c,a):
    print("hi",a,"to",b,"livewire",c)
a="name"
b="favoo"
c=1234
soul(a,b,c)


#passing parameter
def example(fname):
    print(fname,"hello")
example("indhu")
example("dhivi")
example("swasti")
example(234)
example("anbu")


#two parameter passing

def funname(fname,lname):
    print(fname+" "+lname)
a=input("enter the name 1")
b=input("enter the name 2")
funname(a,b)

#keyword arguments
def my_func(*elements):
    print(elements[1])
    print(elements[2])
    print(elements[0])
my_func('au','bn','ch')

def my_func(**values):
    print(values["name1"])
    print(values["name2"])
    print(values["name1"])

my_func(name1="swathi",name2="indhu",name3="swetha")


#return funtion
def range(a,b):
    c=a+b
    return c
a=range(32,54)
print(a*10)
b=range(67,34)
print(b/10)


def func(a=32):
    print(a)
func(54)
func(392)
func()


def my_func(country="INDIA"):
    print("i am from",country)
my_func("SWITZERLAND")    
my_func("south africa")
my_func()




#function recursion
def factorial(x):
    if x==2:
        return 2
    else:
        return(x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial (num))

def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))


#lambda function
def x(a):
    return a+2
print(x(58))

x=lambda a:a+15
print(x(92))

x=lambda a,b,c,d:a*b*c*d
print(x(2,9,2,3))

def myfunc(n):
    return lambda a:a*n
m=myfunc(45)
print(m(2))
print(m(3))


#mapping and filtering
data=[4,6,3,4,5]
result1=map(lambda x:x*5,data)
print(list(result1))

result2=filter(lambda x:x%3==0,data)
print(list(result2))

x=lambda a:a*9
print(x(9))

value=[2,3,4,5,6]
result=filter(lambda a:a%2==1,value)
print(list(result))

def a(x):
    return x*3
print(a(9))

a=lambda z:z*7
print(a(6))












