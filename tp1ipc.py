import random
from re import A
def sacar_carta():
    carta = random.randint(1,10)
    return carta

cantidad_cartas_crupier = []
cantidad_cartas_usuario = []
dinero = 500

print ("Bienvenid@ a la mesa de Easy 21")
print("")
print ("Empieza la partida")

carta1 = sacar_carta()
cantidad_cartas_crupier = carta1
print (f"El crupier saca un {carta1} su total es [{cantidad_cartas_crupier}]")

quiere_apostar = input ("¿Quiere apostar? (s/n) ")

while quiere_apostar == "s":
    cantidad_dinero = int(input ("¿Cuanto quiere apostar? "))
    if cantidad_dinero <= dinero:
     print ("---")
    elif cantidad_dinero > dinero:
        print ("No tienes esa cantidad de dinero")
        print ("----")
    quiere_apostar == "s"
    break

if quiere_apostar == "n":
    print ("----")

carta_usuario1 = sacar_carta()
print (f"Usted saca un {carta_usuario1}, su total es {carta_usuario1}")
print (f"Por el momento sacó las cartas [{carta_usuario1}]")

seguir = input("¿Quiere otra carta? (s/n) ")
carta_usuario2 = sacar_carta()
cantidad_cartas_usuario = carta_usuario1 + carta_usuario2
while seguir == "s":
    print (f"Usted saca un {carta_usuario2}, su total es {cantidad_cartas_usuario}")
    print (f"Por el momento sacó las cartas [{carta_usuario1},{carta_usuario2}]")
    if seguir == "s":
        break
    if (cantidad_cartas_usuario)>= 21:
        print ("La suma de sus cartas supero 21. Usted pierde")
if seguir == "n":
    print ("----")
   
carta_usuario3 = sacar_carta()
suma_de_usuario2 = cantidad_cartas_usuario + carta_usuario3
seguir2 = input("¿Quiere otra carta? (s/n) ")
 
if (cantidad_cartas_usuario) >= 21:
    print ("La suma de sus cartas supero 21. Usted pierde")
elif (cantidad_cartas_usuario) <= 21:
    while seguir2 == "s":
        print (f"Usted saca un {carta_usuario3}, su total es {suma_de_usuario2}")
        print (f"Por el momento sacó las cartas [{carta_usuario1},{carta_usuario2},{carta_usuario3}]")
        if seguir == "s":
            break
if seguir2 == "n":
    print ("----")

if (suma_de_usuario2) >= 21:
    print ("La suma de sus cartas supero 21. Usted pierde")