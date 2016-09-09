def euclides(max, min):
	if max < min:
		temp = max; max = min; min = temp 
	a = int(max / min) 
	r = max % min
	print(str(max) + ' = ' + str(min) + ' * ' + str(a) + ' + ' + str(r))
	if r == 0:
		return min
	max = min
	min = r
	return euclides(max, min)

print("Este programa calcula de manera recuersiva el MCD\n"+
	"entre 2 números dados utilizando el Teorema de Euclides\n")
print("A continuación se le pedirá ingresar 2 valores numéricos: \n")

a = int(input("Primer número: "))
b = int(input("Segundo número: "))


print("\nProcedimiento: "+"\n")

mcd = euclides(a, b)

print("\nEl MCD de "+str(a)+" y "+str(b)+" es: " + str(mcd))
if mcd == 1:
	print("Por lo cual son primos relativos.")