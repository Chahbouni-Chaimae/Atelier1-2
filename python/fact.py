def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=5
print("le factorial de ", num, "est" , factorial(num))

def somme_factorial(s,x):
    s=0
    s=s+(factorial(x)/x)
n=int(input("entrez un nombre:"))   
for x in range(0,n-1):
 print("la somme des séries est:" , somme_factorial(x))