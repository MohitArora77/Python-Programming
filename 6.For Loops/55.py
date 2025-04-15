a="nitin is good ava aba".split()
out=" "
for i in a:
    if i==i[::-1]:
        out+=i
        out+=" "
print(out)