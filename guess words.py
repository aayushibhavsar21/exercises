
print("_____In this game system will guess word from given words list and user has to recognize alphabet from it_____")

words = ['abc', 'def', 'ghi', 
         'jkl','mno', 'pqr']

name = input("what is ypur name ?")
print("hello ",name)

turns=5

while turns>=0:
    print(f"you have {turns} turns left")
    guess = input("guess any alphabet :")
    fail = 0
    win = 0

    for word in words:
        for char in word:
            if char == guess:
                print(f"your guess is right. word is {word}")
                win = 1 
                break
    
        if win == 0:
            fail = 1
    
    if win == 1:
        break

    if fail == 1:
        print("your guess is wrong :(\n")
        turns-=1

if turns == -1:
    print ("sorry you can not guess any right alphabet :(")
