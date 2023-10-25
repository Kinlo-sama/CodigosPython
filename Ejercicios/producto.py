def ver(vector):
	print("<",end="")
	for i in vector:
		print(i,end=" ")
	print(">",end="")

v1 = {2,8,9,7,5}
v2 = {4,8,2,5,1}
ver(v1)
ver(v2)
print("")
suma = 0
for i,j in enumerate(zip(v1,v2)):
	suma += j [0] * j[1]
print(suma)
