a=int(input("enter first value::"))
b=int(input("enter second value::"))
c=input("press + / * - to perform operation")
if(c=='+'):
     print(a+b)
elif(c=='-'):
     print(a-b)
elif(c=='*'):
     print(a*b)
elif(c=='/'):
     print(a/b)
else:
     print("enter valid input")
