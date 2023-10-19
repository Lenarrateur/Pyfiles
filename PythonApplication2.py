###
message ='Good Morning'
print(len(message))
#strat at G=0
print(message[8])
print(message[0:3])
#0 character included, 3rd character excluded
#if blank, frome the start/to the end of the string
print(message[0:])
print(message[0:-1])
print (message.count('g'))
print (message.find('o'))
#retourne l'index du premier 'o'
message2 = message.replace('Morning', 'Afternoon')
print(message2) 

if message2=='Its me':
    print('Me')
elif message2=='Its me again':
    print('else')
else :
    print('stop')
    

weight = float(input('What is your weight ?'))
height = float(input("What is your height")[:-1])
if height> 100:
    height=height/100
if (weight/height/height) <18.5:
    print("You're underweight")
elif (weight/height/height) <25:
    print( "You're normal, average, in a word boring. But at least in good health.")
elif (weight/height/height)< 30:
    print("You're Overweigth")
else :
    print ("Obesity detected")
    
n1 = int (input("FIRST NUMBER"))
n2 = int (input ("Second Number"))
if n1%n2 == 0 :
    print ("Divisible")
else :
    print (n1%n2)

n1 = int (input("FIRST NUMBER"))
n2 = int (input ("Second Number"))
n3 = int (input ("Third Number"))
if n1>n2 and n1>n3 :
    print (n1 + "Is the max")
elif n2>n3 :
    print (n2 + "is the max")
else :
    print (n3)
 
unitnumber = int(input("Consumption ?"))
if unitnumber<100 :
    print ("O")
elif unitnumber<200 :
    print((unitnumber-100)*5)
else :
    print((unitnumber-200)*10+500)