with file('data.txt') as f:
	data = [ int(d.strip()) for d in f.readlines()]
print sum(data).__str__()[:10]