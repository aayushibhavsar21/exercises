
print("__________Kon banega carodpati__________")

que1 = [["1. The national game of india :","\na.cricket","\tb.football","\nc.hocky","\td.tenis","c"],
["2. The national animal of india :","\na.lion","\t\tb.tiger","\nc.leopard","\td.fox","b" ],
["3. The national bird of india :","\na.sparrow","\tb.peacock","\nc.parrot","\td.crow","b" ],
["4. The national tree of india :","\na.banyan","\tb.peepal","\nc.neam","\t\td.mango","a" ],
["5. The national flower of india :","\na.rose","\t\tb.mogra","\nc.sunflower","\td.lotus","d" ],
["6. The national fruits of india :","\na.mango","\tb.apple","\nc.watermelon","\td.banana","a"]]
price=[1000,2000,3000,4000,5000,6000]
i=0
count=0
while i<len(que1):
    que=que1[i]
    print("\nagla sawal ",price[i]," rupeeyo ke liye aap ki screen pr ye raha :")
    print(que[0],que[1],que[2],que[3],que[4],"\n write your ans from a to d :")
    ele=input()
    if ele==que[5]:
        print("sahi jawab..!! :)")
        count=count+1
    else:
        print("galat jawab.. :-(")
        break 
    i=i+1   

money=0
for i in range(count):
    money=money+price[i]

if(count==6):
    print(" congratulation..!! you have successfully answered all the questions: ")
    
print("\nyou have ",money," as your winning price.. :)")

