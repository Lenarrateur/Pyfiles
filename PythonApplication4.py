
n = int (input ("Enter the value of n:"))
for i in range (1, n+1, 2):
    n=n*2
print (n)

sum=0
for i in range(6):
    sum=sum +i
    print(f"The value of sum in each iteration: {sum}")
print ("The sum is valid {}".format (sum))

prod = 0
n= int(input("Value of n ?"))
for i in range(n+1):
    prod = prod + i
print (prod)

for i in range (4) :
    for j in range (3):
        print ("i = {}, j ={}".format (i, j))
        
n = int(input("Enter a positive integer:"))
sum = 0
for j in range (1, n+1):
    q =(j+1)/ j**2
    sum =sum+q
print ("For n={} the sum is {: .2f}". format(n, sum))
#The .2f specifies 2 decimal places. For ecample, .0f will give 4, .1f 4,5 ...  

factoriel =1
for j in range (1, n+1):
    factoriel = factoriel *j
print ("{} factorial is {}". format (n, factorial))


for j in range (1, 10):
    for q in range (1, 10):
        if (q!=j):
            print("{}{}".format(j,q))
            

a = int (input("Enter the numb of triangle"))
for i in range(0,a+1):
    t=i*(i+1)/2
print (t)

for i in range(0,10):
    for q in range(0,10):
        for j in range(0,10):
            if (i*100+q*10+j)==(i**3+j**3+q**3):
                print("{}{}{}".format(i,q,j))
                
num =int(input("number of odd numbers ?"))
sum=0
for i in range (0, num+1):
    sum=sum+2*i+1
print ("The sum of the first {} odd numbers is {}".format(num,sum))
            
num =int(input("number to test ?"))
alpha = True
for i in range (2, num -1):
    if num%i == 0:
        alpha = False
print(alpha)

a=0
b=1
num =int(input("Fibonnaci value"))
for i in range (num):
    c=a+b
    a=b
    b=c
print (b)