
#Exercice 2

test = {"Anz" : {1 : 2.3, 3: 4.1} , "Bank of Australia" : {1 : 0.1, 3: 5}, "Commonwealth Bank" : {1 : 3.5, 3: 3.8}, "Welstpac" : {1 : 3.7, 3: 3.7}}
value = input ("Quelle est la banque ?")
value5 = int(input("How many years ?"))
if (value5<=2) :
    value4=1
else : 
    value4=2
print ("The interest rate is :".format((test[value][value4]*12)))

#Exercice 1

test2 = {"H" : {"Symbol" : "H", "Melting" : 14, "Boiling" : 20},"He" : {"Symbol" : "He", "Melting" : 1, "Boiling" : 4},"Li" : {"Symbol" : "Li", "Melting" : 453, "Boiling" : 1603},"Be" : {"Symbol" : "Be", "Melting" : 1560, "Boiling" : 2742}}
value2 = input ("Symbol ?")
boil = test2[value]["Boiling"]
melt = test2[value]["Melting"]
value3 = input ("Temp ?")
if (value3<= melt):
    print("solid")
else :
    if (value3<= boil):
        print("liquid")
    else :
        print("gaz")


def myf (fname, lname):
  print (fname +" "+ lname)
  
myf("Mathys", "George")

def myf2 (*kids):
  print ("The youngest child is" + kids[2])  
myf2("Emil","Tobias","Linus")

#pour avoir des dictionnaire en input, **

def myf3(**kid) :
   print("His last name is "+ kid ["lname"]) 
   
myf3(fname = "Tobia", lname = "Refsnes")

def myf4(fname2 = "Luls", lname2 = "ayz"):
   print (fname2 + " " + lname2)  
   
myf4("Emily")

def myf5(x):
   return(5 *x)   

print(myf5(3))

def myf6():
  pass


def myf7():
 print("Hello grom a function")   
 

def myf8(x,y):
  if x>y:
    return (x)
  else :
   return (y)
  
print(myf8(5,8))
    
def myf8(*number) :
  max = number [0]
  min = number [0]
  for x in number :
     if x>max:
       max = x
     if x<min:
       min = x
  print (max, min)
  
myf8(2,5,3,4,6,8.2,3,2,6)

try:
  f = open('/content/test_file.txt')
  var = bad_var
except FileNotFoundError:
  print('Sorry. This file does not exist')  
except NameError:
  print ("Something went wrong")
finally:
   print("This is final")  
   

