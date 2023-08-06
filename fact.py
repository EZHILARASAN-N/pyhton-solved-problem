print("----------factorial----------")
num=int(input("enter the number :"))
fact=1
if(num<0):
    print("factorial is not find")
elif(num==0):
    print(num,"factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print(fact)   
print("--------factorial is succesfully-----------")             