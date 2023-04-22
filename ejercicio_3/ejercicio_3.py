print("------------------------")
print("---------DADOS----------")
print("------------------------")

#input
import random
c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""

n = int(input("ingrese la cantidad de veces que va lanzar los dados: "))

#processing

for i in range(n):
    cd = random.randint(1,6)
    if cd == 1:
        c1 += "*"
    elif cd == 2:
        c2 += "*"
    elif cd == 3:
        c3 += "*"
    elif cd == 4:
        c4 += "*"
    elif cd == 5:
        c5 += "*"
    elif cd == 6:
        c6 += "*"

#output

print(f"""
1 = {c1}
2 = {c2}
3 = {c3}
4 = {c4}
5 = {c5}
6 = {c6} """)
