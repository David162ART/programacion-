import ahorcado
import adivinanza

print("____________________")
print("ELIJA SU JUEGO")
print("____________________")

print("(1) AHORCADO (2) adivinanza")


juego = int(input("Cual juego ?"))


if (juego ==1):
    print("jugando horca")
    ahorcado.jugar_ahorcado()
elif (juego==2):
    print("jugando adivinanza")
    adivinanza.jugar_adivinanza()