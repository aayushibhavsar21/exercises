

class library:

    def __init__(self):
        self.book=[]
        self.no_of_book=0

    def add(self,new_book):
        self.book.append(new_book)
        self.no_of_book = self.no_of_book + 1

    def show(self):
        print("list of books:",self.book,"\nnumber of book:",self.no_of_book)

    def check(self):
        if self.no_of_book==len(self.book):
            print('equal')
        else:
            print("not equal")

a=library()
while True:
    x=int(input("\n1.add new book.\n2.print books.\n3.check size of book and no of book.\n4.exit.\npress one number from 1 to 4:"))

    match x:
        case 1:
            name=input(print("enter book name:"))
            a.add(name)

        case 2:
            a.show()

        case 3:
            a.check()

        case 4:
            break

        case _:
            print("wrong input")
