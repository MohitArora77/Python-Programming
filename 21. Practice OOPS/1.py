class library:
    
    # l_name="ABC_LIB"
    # l_loc="Delhi"
    book_dict={'python':6,'Java':2,'SQL':10,'JS':4,'C++':8}
    
    def student_info(self,name,std_ID,phno,number_of_books=[]):
        self.name=name
        self.std_ID=std_ID
        self.number_of_books=number_of_books
        self.phno=phno
                
    def disp_obj(self):
        print(self.name,self.std_ID,self.number_of_books)
        
    def deposite_book(self):
        bn=int(input("Enter the Book :"))
        self.number_of_books.remove(bn)
        self.book_dict[bn]+=1
        
    def withdraw_book(self):
        bn=input("Enter the number :")
        if bn in self.book_dict and self.book_dict[bn]>0:
            self.number_of_books.append(bn)
            self.book_dict[bn]-=1
        else:
            print("nan")

obj1= library('XYZ',765,9878767656)


while True: 
    print("1. Return_BOOK")
    print("2. GET_BOOK")
    print("3. STUDENT INFO ")
    print("4. EXIT ")
    num=int(input("Enter the number:"))

    if num == 1:
        obj1.deposite_book()
    elif num == 2:
        obj1.withdraw_book()
    elif num == 3:
        obj1.disp_obj()
    elif num == 4:
        break
    else:
        print(obj1.book_dict)