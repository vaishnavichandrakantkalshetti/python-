s="This Is Book"

d={"UPPERCASE":0,"LOWERCASE":0}
for i in s:
    if i.isupper():
        d["UPPERCASE"]+=1
    elif i.islower():
        d["LOWERCASE"]+=1
    else:
        pass
print("original string is",s)
print("no.of Uppercase characters are",d["UPPERCASE"])
print("no.of Lowercase characters are",d["LOWERCASE"])
