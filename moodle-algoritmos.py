'''
#algoritmo chatGPT
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        medio = b
        mayor = c
    else:
        medio = c
        mayor = b

elif b <= a and b <= c:
    menor = b
    if a <= c:
        medio = a
        mayor = c
    else:
        medio = c
        mayor = a

else:
    menor = c
    if a <= b:
        medio = a
        mayor = b
    else:
        medio = b
        mayor = a

print("Números ordenados de menor a mayor:", menor, medio, mayor)

'''

'''
#algoritmo gemini
def ordenar_con_condicionales(a, b, c):
    # Caso 1: 'a' es el menor
    if a <= b and a <= c:
        if b <= c:
            return a, b, c
        else:
            return a, c, b
            
    # Caso 2: 'b' es el menor
    elif b <= a and b <= c:
        if a <= c:
            return b, a, c
        else:
            return b, c, a
            
    # Caso 3: 'c' es el menor
    else:
        if a <= b:
            return c, a, b
        else:
            return c, b, a

# Prueba del algoritmo:
print(ordenar_con_condicionales(42, 12, 25))  # Salida: (12, 25, 42)
'''