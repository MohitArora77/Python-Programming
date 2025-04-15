
#Initialising property using Function
class bank:
    bname="ICICI"
    bloc="meerut"
    bIFSC= "ICICI000N1245"
    
    def sam(obj,name,addr,phno,addhar,PAN,email): #object memberes dec in a function
        obj.name=name
        obj.addr=addr
        obj.phno=phno
        obj.addhar=addhar
        obj.PAN=PAN
        obj.email=email
        obj.name=name
     # objects   
harsh=bank()
babu=bank()
 # to declare values for the objects in a fuction 
harsh.sam('harsh','sector-22',9898765678,354676574876,"GWOS3DK5442",'hars23h@gmail.com')
babu.sam('babu','sector-22',8766876898,786565456785,"FSRG23GH2228","babu345@gmail.com")
print(bank.bname,bank.bloc,bank.bIFSC)
print(harsh.name,harsh.addr,harsh.phno,harsh.email,harsh.PAN)