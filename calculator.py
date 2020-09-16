'''
Collaborators: 
Kasey

'''
def addition(num1,num2):
    add=num1+num2
    return add
def subtract(num1,num2):
    sub=num1-num2
    return sub
def multiply(num1,num2):
    mult=num1*num2
    return mult
def divide(num1,num2):
    div=num1/num2
    return div



num1=int(input("enter a number"))
num2=int(input("enter another number"))
asmd=int(input("enter 1 to add, 2 to subtract, 3 to mulitply, or 4 to divide"))

if asmd==1:
    print (num1,"+",num2,"=",(addition(num1,num2)))
elif asmd==2:
    print (num1, "-", num2, "=", subtract(num1,num2))
elif asmd==3:
    print (num1, "*", num2, "=", multiply(num1,num2))
elif asmd==4:
    print (num1, "/", num2, "=", divide(num1,num2))
    
    


       


