# ejercicio 1

pares = 0
impares = 0 
m = int(input("ingrese la cantidad de numeros a evaluar:\n"))
for i in range(m):
    N = int(input("digite un numero: "))
    if N % 2 == 0:
        pares +=  1
    else:
        impares += 1
print(f"{pares} numero son pares")
print(f"{impares} numeros son impares")