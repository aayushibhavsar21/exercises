
print("________Secret code language________")

msg=input("enter your message:")

print("____encoding____")
words=msg.split()
new_msg=""
import random
for word in words:
    if len(msg)>2:
        str1=" "
        for i in range(3):
            num=random.randint(97,122)
            str1=str1+chr(num)

        str2=" "
        for i in range(3):
            num=random.randint(97,122)
            str2=str2+chr(num)

        word=str1+word[1:]+word[0]+str2
        word=word.replace(" ","")
        new_msg=new_msg+" " +word
    else:
        new_msg=msg[::-1]
print("encoded message:",new_msg)

print("____decoding____")
msg=""
if len(new_msg)>2:
    words=new_msg.split()
    for word in words:
        word=word[3:-3]
        msg=msg+" "+word[-1]+word[0:-1]
else:
    msg=new_msg[::-1]        
print("decoded message:",msg)

