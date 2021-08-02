class Library():

    def __init__(self,list):

        self.booklist=list

        self.lendict={}



    def displaybook(self):

        print(f"We have following books in our library")

        for book in self.booklist:

            print(book)





    def lendbook(self,user,book):

        if book not in self.booklist:

            print("Book is not available, Kindly choose the book from the Book list")

            

        else:

            self.lendict.update({user:book})

            print("Lender-Book database has been updated. You can take the book now")

            



    def addbook(self,book):

        self.booklist.append(book)

        print("Book has been added to the book list")





    def returnbook(self,user):

        print(f"{self.lendict[user]} book returned")

        self.lendict.pop(user)



    def disp(self):

        print("User Name and the Book used")

        for k, v in self.lendict.items():

            print(k+":"+v)



if __name__=='__main__':

    print("Welcome to Central Library:")

    store=Library(['Rich Daddy Poor Daddy','Ikigai','Girl On The Train','Apple','C Programming','Alchemist','Adultery','13 Resons Why'])

    while(True):

        

        print("\n--Enter your choice--")

        print("1. Display Books")

        print("2. Lend a Book")

        print("3. Add a Book")

        print("4. Return a Book")

        print("5. Display Users and Books used")

        n=int(input())



        if n==1:

            store.displaybook()



        elif n==2:

            user=input("Enter your name: ")

            book=input("Enter the name of the book you want to lend: ")

            store.lendbook(user,book)

            



        elif n==3:

            book=input("Enter the name of the book you want to add: ")

            store.addbook(book)



        elif n==4:

            user=input("Enter your Name: ")

            store.returnbook(user)



        elif n==5:

            store.disp()



        else:

            print("Not a valid option")



        n1=input("\nEnter c to continue and q to quit: ")

        if n1=="c":

            continue

        if n1=='q':

            exit()
