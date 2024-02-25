#1) Básico: imprime todos los números enteros del 0 al 150.
i = 0
while i < 151:
    print(i)
    i += 1

for i in range(151):
    print(i)

#2) Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1000.
i = 0
while i < 1001:
    if i % 5 == 0:
        print(i, 'multiplo de 5')
    i += 1

for i in range(1001):
    if i % 5 == 0:
        print(i, 'multiplo de 5')
    else:
        continue

#3) contar, a la manera de dojo: imprime números enteros del 1 al 100.
# Si es divisible por 5, imprime "Coding" en su lugar. Si es divisible por 10, imprime "Coding Dojo"
i = 0
while i < 101:
    if i % 10 == 0:
        print(i, 'Coding Dojo')
    elif i % 5 == 0:
        print(i, 'Coding')
    i += 1

for i in range(100+1):
    if i % 10 == 0:
        print(i, 'Coding Dojo')
    elif i % 5 == 0:
        print(i, 'Coding')

#4) Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500.000 e imprime la suma final
i = 0
suma = 0
for i in range(500001): 
    if i % 2 != 0:
        print(f'{i} es impar')
        suma += i
print(suma)

i = 0
suma = 0
while i < 500001:
    if i % 2 != 0:
        print(f'{i} es un numero impar')
        suma += i
    i +=1
print(suma)

#5) Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018,0,-4):
    print(i)


#6) Contador flexible: establece tres variables de mult. Por ejemplo, si lowNum = 2, higNum = 9 y mult = 3. 
# El bucle debe imprimir 3,6,9 (en lineas sucesivas).

lowNum = 2
highNum = 9
mult = 3
while lowNum < highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1
else:
    print(lowNum)


for i in range(lowNum, highNum + 1, 1):
    if i % mult == 0:
        print(i)
