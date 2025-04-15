class upper:
    upper_ch="ABCDEFGHIJFKLMNOPQRSTUVWXYZ"
class lower:
    lower_ch="abcdefghijklmnopqrstuvwxyz"
class num:
    number="0123456789"
class char(upper,lower,num):
    s_chr="_$"

print("UPPER:",char.upper_ch,end=" ")
print("lower:",char.lower_ch,end=" ")
print("Numbers:",char.number,end=" ")
print("S_chr:",char.s_chr,end=" ")
    