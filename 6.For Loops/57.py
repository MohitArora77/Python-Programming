# WAP to take a string remove duplicate spelling from it.
a="hello"
out=" "
for i in a:
    if i not in out:
        out+=i
print(out)

    