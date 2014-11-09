alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i= 1
c= {}

for a in alphabet:
    c[a]=i
    i += 1
def sum(str):
    total = 0
    for s in str:
        total += c[s]
    return total
    
    
with file('p022_names.txt') as f:
    data = f.readlines()
f.closed
i = 1
data = data[0].replace('"',"").split(',')
data.sort()
total = 0
for name in data:
    total += sum(name) * i
    i += 1
print total