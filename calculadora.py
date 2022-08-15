#Calculadora con condicionales.

print('''Seleccione la operación desea realizar:

SUMA = S o s
RESTA = R o r
MULTIPLICACION = M o m
DIVISION = D o d''')

eleccion = input('\nIngrese su elección: ').lower()

if eleccion =='s':
    print('Usted eligio sumar')
    a = float(input('\nIngrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    r = a + b
    print(f'El resultado es: {r:.2f}')
elif eleccion =='r':
    print('Usted eligio restar')
    a = float(input('\nIngrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    r = a - b
    print(f'El resultado es: {r:.2f}')
elif eleccion =='m':
    print('Usted eligio Multiplicar')
    a = float(input('\nIngrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    r = a * b
    print(f'El resultado es: {r:.2f}')
elif eleccion =='d':
    print('Usted eligio Dividir')
    a = float(input('\nIngrese el primer numero: '))
    b = float(input('Ingrese el segundo numero: '))
    r = a / b
    print(f'El resultado es: {r:.2f}')
else:
    print('Elija una opción correcta')
