name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d={}
for i in handle:
    if i.startswith("From "):
        name=i.split()[1]
        d[name] = d.get(name,0) + 1
#print(d)
user = max(d.items(),key=lambda x:x[1])
print(user[0],user[1])
