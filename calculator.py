'''
Collaborators: 
Kasey

'''
def addition():
    add=num1+num2
    return add
def subtract():
    sub=num1-num2
    return sub
def multiply():
    mult=num1*num2
    return mult
def divide():
    div=num1%num2
    return div



num1=int(input("enter a number"))
num2=int(input("enter another number"))
asmd=int(input("enter 1 to add, 2 to subtract, 3 to mulitply, or 4 to divide"))

if asmd==1:
    print (addition())
elif asmd==2:
    print (subtract())
elif asmd==3:
    print (multiply())
elif asmd==4:
    print (divide())
    
    


       



