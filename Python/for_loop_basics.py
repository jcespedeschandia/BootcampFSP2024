#1) Básico: imprime todos los números enteros del 0 al 150.
for i in range(151):
    print(i)



#2) Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1000.
v = 5
for i in range(100):
    if i%v == 0:
        print(i)

#3) contar, a la manera de dojo: imprime números enteros del 1 al 100.
# Si es divisible por 5, imprime "Coding" en su lugar. Si es divisible por 10, imprime "Coding Dojo"
v = 5
x = 10
for i in range(1,100):
    if i%x == 0:
        print(i,"Coding Dojo")
    elif i%v == 0:
        print(i,"Dojo")
    else:
        print(i)


#4) Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500.000 e imprime la suma final
suma_impares = 0
rango = 500000
for i in range(0,rango):
    if i%2 != 0:
        suma_impares += i
print(f'La suma total de los impares desde 0 a {rango} es: {suma_impares}')

#5) Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018, 0, -4):
    print(i)

#6) Contador flexible: establece tres variables de mult. Por ejemplo, si lowNum = 2, higNum = 9 y mult = 3. 
# El bucle debe imprimir 3,6,9 (en lineas sucesivas).
lowNum = 3
highNum = 9
mult = 3
for i in range(lowNum, highNum +1):
    if i % mult == 0:
        print(i)
