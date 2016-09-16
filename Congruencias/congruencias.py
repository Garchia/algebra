# Work in progress

n = 3
c = ['' for i in range(0, n)]
c[0] = "3mod5"
c[1] = "2mod7"
c[2] = "5mod11"

rem = [0 for i in range(0, n)]
mod = [0 for i in range(0, n)]

for i in range(0, n):
	st = c[i].split("mod")
	rem[i] = int(st[0])
	mod[i] = int(st[1])

# z = X1B1C1 + . . . + XnBnCn

B = 1
for i in range(0, n):
	B *= mod[i]

print(B)

Bi = [0 for i in range(0, n)]
for i in range(0, n):
	Bi[i] = B // mod[i]

print(Bi)

# X1B1 = 1 mod 5
"""
	X1B1 = 1 mod 5
	B1 = 77
	r = 1

	77(X1) = r(mod 5)

	77 // 5 = 15 * 5 = 75
	-75
	2(X1)  = 1(mod 5)
			 +5
	2(X1)  = 1+5 (mod 5)
	2(X1)  = 6 (mod 5)
	2(? )  = 6

	X1 = 3

	X2B2 = 1 mod 7
	55(X2) = 1 mod 7

	55 // 7 = 7 * 7 = 49
	-49
	6(X2) = 1 mod 7
			+35
	6(X2) = 36 mod 7

	X2 = 6

	35(X3) = 1 mod 11
	-33
	2(X3) = 1 mod 11
			+11
	2(X3) = 12 mod 11

	X3 = 6 

"""

Xi = [3, 6, 6]

z = 0
for i in range(0, n):
	z += Xi[i] * Bi[i] * rem[i]

print(z)

def confirm(z):
	if (z % mod[0] == rem[0] and
		z % mod[1] == rem[1] and
		z % mod[2] == rem[2]):
		return True
	return False

print(confirm(z))

sol = 0

def result():
	sol = z % B
	return str(sol) + ' + ' + str(mod[0]) + '*' + str(mod[1]) + '*' + str(mod[2]) + ' is a solution.'

print(result())
print(sol % mod[0], sol % mod[1], sol % mod[2])

def are_relative_primes(modulos):
	if (euclides(mod[0], mod[1]) == 1 and 
		euclides(mod[0], mod[2]) == 1 and 
		euclides(mod[1], mod[2]) == 1):
		return True
	return False

def euclides(max, min):
	if max < min:
		temp = max; max = min; min = temp 
	a = int(max / min) 
	r = max % min
	if r == 0:
		return min
	max = min
	min = r
	return euclides(max, min)

print(are_relative_primes(mod))
print(rem, mod)
