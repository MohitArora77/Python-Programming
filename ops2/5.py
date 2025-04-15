class Bank:
    bname="Kotak"
    bIFSC=8739847823
    baddr="Delhi"
    bmanager="MR. ABC"
    
ob1=Bank()
ob2=Bank()
ob3=Bank()
ob4=Bank()
ob5=Bank()

ob1.name="XYZ"
ob1.accno=908098987876
ob1.phno=9878767656
ob1.addr="Indrapuram"
ob1.aadharno=987687657654
    
ob2.name="BCD"
ob2.accno=9876278463276324
ob2.phno=7865765747
ob2.addr="Delhi"
ob2.aadharno=789667856785

ob3.name="EFG"
ob3.accno=9876278463276324
ob3.phno=7865765747
ob3.addr="Noida"
ob3.aadharno=789623423432

ob4.name="HIJ"
ob4.accno=98762324623784
ob4.phno=78657632874
ob4.addr="Ghaziabad"
ob4.aadharno=736552654723

ob5.name="KLM"
ob5.accno=9876278327532654
ob5.phno=7866787656
ob5.addr="Kolkata"
ob5.aadharno=327467863713

print("Class Member/ Class Properties :")
print("-"*50)
print(Bank.bname,Bank.bIFSC,Bank.baddr,Bank.bmanager)
print("="*50)
print("Obejct Members/ Object Properties :")
print("-"*50)
print(ob1.name,ob1.accno,ob1.phno,ob1.addr,ob1.aadharno)
print(ob2.name,ob2.accno,ob2.phno,ob2.addr,ob2.aadharno)
print(ob3.name,ob3.accno,ob3.phno,ob3.addr,ob3.aadharno)
print(ob4.name,ob4.accno,ob4.phno,ob4.addr,ob4.aadharno)
print(ob5.name,ob5.accno,ob5.phno,ob5.addr,ob5.aadharno)
print("-"*50)