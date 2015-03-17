with file("p067_triangle.txt") as f:
	p = [[int(x) for x in f.strip().split(' ')] for f in f.readlines()]

def createstart(len):
	r = []
	for l in range(1,len+1):
		r.append([0]*l)
	return r

s= createstart(len(p)) 
s[0][0] = p[0][0]
for i in range(1,len(p)):

	for v in range(0,len(p[i])):
		val = p[i][v]
		if v<i:
			local = val + s[i-1][v]
			s[i][v] = max(local,s[i][v])
		if v>=1:
			local = val + s[i-1][v-1]
			s[i][v] = max(local,s[i][v])
print max(s[-1])
		