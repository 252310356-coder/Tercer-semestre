#Creacion de lista

puntuaciones = [150,200,85,300,120]
print ("Puntuaciones iniciales: ", puntuaciones)

#Acceso por indice

primer_jugador= puntuaciones[0]
ultimo_jugador= puntuaciones[-1]

suma= primer_jugador + ultimo_jugador

print (f"primer jugador {primer_jugador} | ultimo jugador {ultimo_jugador}")

print (f"Suma de ambos puntajes: {suma}")

#Modificaciones por indice
puntuaciones[2] = 100

#Nuevo valor al final
puntuaciones.append(250)

print ("Lista corregida y actualizada: ", puntuaciones)

#Recorrido de lista

for categoria, puntos in enumerate (puntuaciones, start=1):
    categoria = "Pro" if puntos >= 200 else "Avanzado"
    print (f"Jugador {categoria}: {puntos} pts({categoria})")

#Desafio
# Inicializar con el primer valor de la lista o con None
# Inicializamos con el primer índice y su valor
indice_bajo = 0
bajo = puntuaciones[0]

for i, puntos in enumerate(puntuaciones):
    if puntos < bajo:
        bajo = puntos
        indice_bajo = i        

print(f"La puntuacion mas baja es: {bajo}")
print (f"index: {indice_bajo}")
puntuaciones.pop(indice_bajo)
print ("Puntuaciones: ", puntuaciones)




print ("Otra actividad")
precios = [100.0, 50.0, 200.0, 75.0]
# Recorrido por índice para modificar la lista en su lugar
for i in range(len(precios)):
 if precios[i] > 80.0:
     precios[i] = precios[i] * 0.9 
 # Se sobreescribe la posición original
print(precios)
# Resultado: [90.0, 50.0, 180.0, 75.0]