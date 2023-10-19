num = int (input ("Enter an integr value:")) 
ndiv= 1

while ndiv<0:
    res = num//ndiv
    print ("The integer division of {} by 3 gives: {}". format (num, res))
    ndiv=ndiv+1
    print ("NUMBER OF DIVISIONS SO FAR: {}".format(ndiv))
    num = int(input("Enter an integer value:"))
    
print ("We're done")
print ("Total number of iteration: {}".format (ndiv))

a= 0
for i in range (10) :
    a=a+i
print (a)

a=0
sum = 0
for i in range (10):
   i= int(input("The Number is ?"))
   sum=sum+i
print (sum/10)

name = 'Jesaa29Roy'
size = len(name)
i=-1
while i<size-1:
    i=i+1
    if not name[i].isalpha():
        continue
    print(name[i], end='')
    print("\nThe execution has stopped")
