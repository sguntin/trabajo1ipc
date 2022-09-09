import random
from re import A
def sacar_carta():
    carta = random.randint(1,10)
    return carta

cantidad_cartas_crupier = []
cantidad_cartas_usuario = []

print ("Bienvenid@ a la mesa de Easy 21")
print("")
print ("Empieza la partida")

a = sacar_carta()
b = sacar_carta()
suma_de_crupier = (a + b)
print (f"El crupier saca un {a} su total es [{a}]")

quiere_apostar = input ("¿Quiere apostar? (s/n) ")
cantidad_dinero = int(input ("¿Cuanto quiere apostar? "))

while quiere_apostar == "s":
    print(cantidad_dinero)
    if cantidad_dinero>500:
     print('no tienes esa cantidad de dinero')
     print('---')
     break
    elif cantidad_dinero <=500:
        print('---') 
        break
