objetivo = int(input('Ingresa un número: '))
epsilon = 0.01
# 0.0001
paso = epsilon**2
respuesta = 0.0
cont = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    cont += 1

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}', cont)
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}', cont)
