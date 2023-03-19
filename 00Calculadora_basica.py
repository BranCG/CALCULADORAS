n1 = input("Escribre el primer número  ")
n2 = input("Escribre el segundo número  ")


n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2
elev = n1 ** n2

mensaje = f"""El resultado de los números {n1} y {n2} son:
El resultado de la suma = {suma},
El resultado de la resta = {resta},
El resultado de la multiplición = {multi},
El resultado de la división = {div},
El resultado {n1} elevado a {n2} = {elev}
"""

print(mensaje)
