print("--------------------------")
print("--------FACTORIAL---------")
print("--------------------------")

#input

n = int(input("ingrese el numero al que desea hayar su factorial: "))
fa = 1
a = 1

# processing
for i in range (n):
    fa = fa*a
    a += 1

#output

print(f"el factorial del numero es {fa}")