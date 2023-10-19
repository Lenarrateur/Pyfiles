#Exercice 1
import numpy as np
vect = np.linspace (1,5,21)
for i in range (21):
    vect[i]=vect[i]/10
print (vect)

#Exercice 2
import numpy as np
import math
x0 = float(input("x0 ?"))
s = float(input("s ?"))
x1 = int(input("Beginning ?"))
x2 = int(input("End ?"))
x3 = int(input("Number of point ?"))
vect = np.linspace (x1,x2,x3)
vect2 = np.zeros(x3)
print ("X-------Y")
for i in range(x3):
    vect2[i]=(1/(2*math.pi)**0.5)*math.exp((-1/2)*((vect[i]-x0)**2)/(s**2))
    if (vect[i])<0 :
         print (round(vect[i],3),"__",round(vect2[i],5))
    else :
         print ("",round(vect[i],3),"__",round(vect2[i],5))
         
#Exercice 3
import numpy as np
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4,
            20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
temp_mar = np.asarray(temp_mar)
mean = temp_mar.mean()
print("The mean is {} ".format(mean))
min = temp_mar.min()
max = temp_mar.max()
for i in range(len(temp_mar)):
    if min == temp_mar[i]:
        indexmin = i
        moismin = months[i]
        
for i in range(len(temp_mar)):
    if max == temp_mar[i]:
        indexmax = i
        moismax = months[i]
print("The minimum is {} in {} ".format(min, moismin))
print("The maximum is {} in {} ".format(max, moismax))

#exercice 4
import numpy as np
nbstd=int(input("Enter the number of students"))
liste=[]
mat=np.zeros((nbstd,4))
for i in range (nbstd):
    theorie=int(input("Enter the theory note of the student"))
    problem=int(input("Enter the problem note of the student"))
    totalmark=(4*theorie+6*problem)/10
    mat[i,0]=i
    mat[i,1]=theorie
    mat[i,2]=problem
    mat[i,3]=totalmark

print(mat)

print()

max=0
min=20
index=0
sum=0
for i in range (nbstd):
    sum+=mat[i,3]
    if(max<mat[i,3]):
        max=mat[i,3]
        index=mat[i,0]
    if(min>mat[i,3]):
        min=mat[i,3]
print(f"maximum total grade : {max}")
print(f"minimum total grade : {min}")

avg=sum/nbstd

print(f"the average is {avg}")