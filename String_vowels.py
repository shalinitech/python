

count=0
vow=0
vowels="a,e,i,o,u"
string=input("Enter the String:")

for i in string:
    if i in vowels:
       count=count+1
       vow=vow+1
print("Vowels in the String: " ,vow, "\nNumber of vowels in thr String :",count)
