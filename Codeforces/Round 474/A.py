'''input
bbcc
'''
def ii():
	return input()
def arr():
	return map(int,ii().split())

s = ii()
a = 0
b = 0
c = 0

for ch in s:	
	if ch =='a':
		a+=1
		if b!=0 or c!=0:
			print("NO")
			exit()
	elif ch =='b':
		b = b+1
		if c!=0:
			print("NO")
			exit()
	else:
		c = c + 1

if a!=0 and b!=0 and c!=0:
	if c == a or c== b:
		print("YES")
		exit()

print("NO")
