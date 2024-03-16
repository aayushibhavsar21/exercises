print("________calculator________")
a=int(input("enter first value: "))
b=int(input("enter second value: "))
s=input("enter opration you want to perform:")

if s =='addition':
    print(a+b)
elif s =='subtraction':
    print(a-b)
elif s =='multiplication':
    print(a*b)
elif s =='division':
    print(a/b)
elif s =='modulus':
    print(a%b)
elif s =='power':
    print(a**b)
elif s =='floor division':
    print(a//b)
else:
    print("enter correct opration.")

