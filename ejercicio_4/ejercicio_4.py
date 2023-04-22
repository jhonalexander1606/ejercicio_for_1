print("--------------------------")
print("--------FACTORIAL---------")
print("--------------------------")

#input

n = int(input("ingrese el numero al que desea hayar su factorial: "))
fa = 1
a = 1

# processing
for i in range (1,n+1):
    fa *= i

#output

print(f"el factorial del numero {n} es {fa}")