print("---------------------------")
print("---------MULTIPLOS---------")
print("---------------------------")

#input

mult7 = 0
mult9 = 0

#processing

for i in range (1000,5000):
    if i % 7 == 0:
        mult7 += 1
    if i % 9 == 0:
        mult9 += 1

#output

print(f"hay {mult7} multiplos de 7 entre 1000 y 5000")
print(f"hay {mult9} multiplos de 9 entre 1000 y 5000")