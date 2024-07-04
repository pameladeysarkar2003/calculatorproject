def add(a,b):
    answer=a+b
    print(str(a)+"+"+str(b)+"="+str(answer))
    
def sub(a,b):
    answer=a-b
    print(str(a)+"-"+str(b)+"="+str(ansswer))

def mul(a,b):
    answer=a*b
    print(str(a)+"*"+str(b)+"="+str(answer))

def div(a,b):
    answer=a/b
    print(str(a)+"/"+str(b)+"="+str(answer))

    print("a.addition")
    print("b.substarction")
    print("c.multiplication")
    print("d.division")
    print("e.exit")

    choice=input("input your choice:")

    if choice=="a" or choice=="A":
        print("Addition")
        a=int(input("input first number:"))
        b=int(input("input second number:"))
        add(a,b)

    elif choice=="b" or choice =="B"
    print("Substraction")
    a=int(input("input first number:"))
    b=int(input("input second number:"))
    sub(a,b)
    elif choic=="c" or choice =="C":
    print("Multiplication")
    a=int(input("input first number:"))
    b=int(input("input second number"))

elif choice=="d " or choice=="D":
print("Division")
a=int(input("input first number:"))
b=int(input("input second number:"))
div(a,b)
elif choice=="e" or choice=="E":
print("program ended")
quit()
