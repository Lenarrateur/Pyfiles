from math import pi


name =4
test = 3
a,b,c = 2,5,7
print ("The name value is {} and the test vaue is {}, so the product is {}.".format(name,test, name*test))
d=complex(a)
print ("The operator \\ make an euclidian div")
print (19/2.5)
#variable = input ("Are we gonna win ?")
variable= "yes"
if (variable == "yes" or variable== "Yes" or variable == "YES") :
	print ("BECAUSE IT IS OUR PROOOOOOOOOJECT")
else:
	print("Shut up, cross the road an find a job, looser")
import math
#n = float (input ("Enter volume"))
h = int(input("h = ?"))
r = int(input("r = ?"))
print ((1/3)*math.pi*r*r*h)
dir (math)
temperature = float(input("Quelle est la temperature en Celsius ?"))
temperature= temperature + 273,15
print ("La temperature en Kelvin est {}.".format(temperature))
cote = float(input("Taille du cote ?"))
print ("Le cube a une aire de {}cm**2 et un volume de {} cm**3.".format(6*cote*cote,cote*cote*cote))
n10 = int(input("Nombre de billets de 10 ?"))
n20 = int(input("Nombre de billets de 20 ?"))
n50 = int(input("Nombre de billets de 50 ?"))
print ("Tu possede actuellement {} euros. Il serait peut etre temps de traverser la rue pour trouver un emploi, non ?".format(n10*10+n20*20+n50*50))
radius = float(input("Give me your radius, Oh circle of the scythe !"))
print ("Your Majesty has a circumference of {} cm and an area of {} cm square, two numbers has heavenly as their is !".format(radius*pi*2,radius*radius*pi))
print ("And if you'll be a sphere... You'll be...{} cm**3 and have an area of{} cm**2".format(4*pi*radius*radius*radius/3,4*pi*radius*radius))

A = float(input("A = ?"))
E = float(input("E = ?"))
T = float(input("T = ?"))
R = 8.31
print(A * math.exp(-E/(R*T)))

cote1 = float(input("Premier cote = ?"))
cote2 = float(input("Length of the second side = ?"))
angle = float(input("angle = ?"))
print ((cote1**2 +cote2**2 -2*cote1*cote2*math.cos(angle*pi/180))**0.5)
