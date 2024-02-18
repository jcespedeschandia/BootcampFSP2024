num1 = 42 # Declaracion de variable 'num1'. inicializacion de numero entero 42 en variable 'num1
num2 = 2.3 # Declaracion de variable 'num2'. inicializacion de numero flotante 2.3 en la variable 'num2'
boolean = True # Declaracion de variable 'boolean'. asignacion del valor True de la variable boolean.
string = 'Hello World' # Declaracion de variable 'String'. Inicializacion de cadena en la la variable 'String'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Declaracion de la variable 'Pizza_toppings'. Inicializacion de arreglo en la variable 'Pizza_toppings'
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Declaracion de la variable 'person'. Inicializacion de diccionario en la variable 'person'.
fruit = ('blueberry', 'strawberry', 'banana') # Declaracion de la variable 'fruit'. Inicializacion de lista en variable fruit.
print(type(fruit)) # Imprimir el tipo de variable que es 'fruit' con la funcion type()
print(pizza_toppings[1]) # Imprimir el valor del indice 1 de la variable compuesta 'Pizza_toppings' 
pizza_toppings.append('Mushrooms') # Agrega el valor 'Mushrooms' a la variable compuesta 'Pizza_toppings'
print(person['name']) # Imprime el indice 'name' de la variable compuesta 'person'
person['name'] = 'George' # Asigna el valor 'George' al indice 'name' de la variable compuesta 'person'
person['eye_color'] = 'blue' # Asigna el valor 'blue' al indice 'eye_color' de la variable compuesta 'person' 
print(fruit[2]) # Imprime el indice 2 de la variable compuesta 'fruit'

if num1 > 45: # Evalua la variable 'num1' si el mayor a 45
    print("It's greater") # en caso de ser cierto, imprime la cadena 'It's greater'
else: # en caso de no ser mayor...
    print("It's lower") # ...Imprimir la cadena 'It's lower. 

if len(string) < 5: # Evalua la longitud de la variable 'string' sea menor a 5
    print("It's a short word!") # en caso de ser cierto, imprimir la cadena "It´s a short word!"
elif len(string) > 15: # evalua nuevamente si la longitud de la variable 'string' en mayor a 15.
    print("It's a long word!") # en caso de ser cierto, imprimir la cadena "It's a long word!"
else: # en caso de que ninguna de las evaluaciones sean ciertas...
    print("Just right!") # ... imprimir la cadena "Just right!"

for x in range(5): # itera en la variable 'x', desde 0 a 5 (6 veces) y de uno en uno.
    print(x) # imprime el valor que tenga 'x' en cada iteracion.
for x in range(2,5): # itera en la variable 'x', desde 2 a 5 (3 veces) y de uno en uno.
    print(x) # imprime el valor de 'x' en cada iteracion.
for x in range(2,10,3): # itera en la variable 'x' dede 2 a 10 y de 3 en 3.
    print(x) # imprime la variable 'x' por cada iteracion.
x = 0 # Declaracion de variable 'x'. Inicializacion de numero entero 0 en la variable 'x'. 
while(x < 5): # Itera mientras la variable 'x' sea menor a 5.
    print(x) #imprime la variable 'x' en cada iteracion.
    x += 1 # suma 1 al valor de la variable 'x' en cada iteracion.

pizza_toppings.pop() # elimina el ultimo valor de la variable compuesta 'pizza_toppings'
pizza_toppings.pop(1) # elimina el indice 1 de la variable compuesta 'pizza_toppings'

print(person) # imprime todo el contenido de la variable compuesta (diccionario) 'person'.
person.pop('eye_color') # elimina el contenido del del indice 'eye_color' de la variable compuesta 'person'
print(person) # imprime todo el contenido de la variable compuesta (diccionario) 'person'.

for topping in pizza_toppings: # itera en la variable topping recorriendo todos los indices  del arreglo 'pizza_topping' 
    if topping == 'Pepperoni': # Evalua si el valor de la variable 'topping' es igual a 'Pepperoni'...
        continue #... continua.
    print('After 1st if statement') # imprime en cada iteracion la cadena 'After 1st if statement.'
    if topping == 'Olives': # evalua si el valor de 'toppinng' es igual a 'Olives'...
        break # finaliza el ciclo for.

def print_hello_ten_times(): # Declaracion de funcion 'print_hello_ten_times'
    for num in range(10): # inicia el ciclo for en la variable 'num' desde 0 a 10 y de uno en uno.
        print('Hello') # imprime la cadena 'Hello' en cada iteracion. 

print_hello_ten_times() # Llamado a la funcion 'print_hello_ten_times'.

def print_hello_x_times(x): # Declaracion de la funcion 'print_hello_x_times'
    for num in range(x): # inicia el ciclo for en la variable 'num' de 0 a lo que reciba como parametro la funcion al llamarla.
        print('Hello') # imprime en cada iteracion la cadena 'Hello' 

print_hello_x_times(4) # inicializa la funcion 'print_hello_x_times' con el valor 4 como argumento.

def print_hello_x_or_ten_times(x = 10): # Declaracion de la funcion 'print_hello_x_or_ten_times()'. Funcion tendra como parametro x y un argumento con el valor por defecto de 10.
    for num in range(x): # inicia el ciclo for en la variable 'num' e itera desde 0 a los que reciba como argumento o en su defecto en 10 y de uno en uno.
        print('Hello') # Imprime la cadena 'Hello' en cada iteracion.

print_hello_x_or_ten_times() # inicializa la funcion 'print_hello_x_or_ten_times()' con ningun argumento.
print_hello_x_or_ten_times(4) # inicializa la funcion 'print_hello_x_or_ten_times()' con 4 como argumento.


"""
Bonus section
"""

# print(num3) 
# num3 = 72 # 
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)