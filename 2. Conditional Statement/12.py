#WAP to create a student report card.
a=int(input("enter the no.:"))
if a>90:
    print("Grade A")
elif a<=90 and a>=80:
    print("Grade B")
elif a<=80 and a>=70:
    print("Grade C")
elif a<=70 and a>=60:
    print("Grade D")
elif a<=60 and a>=40:
    print("Grade E")
elif a<=30:
    print("Grade F")    