#j = []

a = "a"
number = 0
while a != "":
    a = input("Number ?")
    if a != "":
        i=int(a)
        j.append(i)
        number=number+1
print("The average is {}".format(sum(j)/number))


j = input("Liste de nom ?")
h= j.split()
num=0
for a in h:
    print ("Hi {}".format(a))
    num=num+1
print ("Salut a vous {}, mes petits jouets".format(num))


Somme=0
a=["H","C","N","O","S","Cl",1.0008,12.011,14.007,15.999,32.065,35.453]
for i in range (6):
    Somme= Somme + int(input("How much {} ?".format(a[i])))*a[i+6]
print (Somme)


n= int(input("What is the max degree ?"))
a =[]
for i in range(n+1):
    a.append(int(input("Coefficient {}?".format(i))))
x= float(input("What is x ?"))
result =0
for i in range(n+1):
    result = result+x**(i)*a[i]
print(result)

  

def add(x,y):
    c=x+y
    return c
print(add(5,4))

