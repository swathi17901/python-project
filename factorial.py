def factorial(x):
    if x==2:
        return 2
    else:
        return(x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial (num))