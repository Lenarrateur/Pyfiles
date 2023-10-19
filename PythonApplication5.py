
a =[1,2,3,7,4,"5"]
#Liste : ordonnée, peut contenir des duplicatas
print(a[2])
for b in a:
    print(b)
a.append('7')
#Add at the end of the list
a.remove(3)
a[3]= 'Notre Projet'
b=(1,4,6,7)
#tupple impossible to change
for j in b:
    print (j)
    
smooth =[3.14, 7, -2 +3j, 'water', False, [1,2]]
print (smooth[2:5])
#Only number 2, 3 and 4

smooth[3][4]

a=[]
u=int(input("Quel est n ?"))
for i in range (1,u+1):
    a.append(1/i)
print(sum(a))

line ="Temperature us 298 K before combustion"
words = line.split (" ")#Separate line into words
print (words)

line = input ("Enter the value separate by a space")
smooth =line.split ()
print ("List is now {}".format (smooth))

a= [1, 3, 5,7,11]
b=[13,17]
c =a+b
print("First Instruction print: {}".format(c))
b[0] =-1
d = []
for e in a:
    d.append(e+1)
print ("Second instruction print: {}".format(d))
d.append(b[0] +1)
d.append(b[-1] +1)
print ("Third print : {}".format(d))
print ("FORTH print : {}".format(d[-2:]))
print ("Fifth : {}".format(d[:-1]))
print ("Six print : {}".format(d[1:4]))

n =int (input("What square do you wish, my lord ?"))
a= []
for i in range (0,n+1):
    a.append(i*i)
print(a)

a=[]
b=[]
moyenne = 0
nombre=0
for j in range (0, 333333):
    n =input("Name ?")
    grade = int(input("grade ?"))
    if (n==""):
      for i in a:
        print (a[nombre],end=' ')
        print (b[nombre])
        nombre=nombre+1
      print (moyenne/nombre)
      break
    else :
      a.append(n)
      b.append(grade)  
      moyenne=moyenne+grade
    
    
    
    