nombre1= input("Cómo se va a llamar el Jugador 1?: ")
nombre2= input("Cómo se va a llamar el Jugador 2?: ")

respuestanombre1 = input("Hola Jugador1 ¿qué eliges: Piedra, Papel o Tijera?: ")
respuestanombre2 = input("Hola Jugador2 ¿qué eliges: Piedra, Papel o Tijera?: ")

condicion1= respuestanombre1 == "Piedra" and respuestanombre2 == "Tijera"
condicion2= respuestanombre1 == "Papel" and respuestanombre2 == "Piedra"
condicion3= respuestanombre1 == "Tijera" and respuestanombre2 == "Papel"

if respuestanombre1 == respuestanombre2:
    print("Ha sigo un empate entre", nombre1, "y", nombre2)
elif condicion1 or condicion2 or condicion3:
    print("Gano", nombre1.lower())
else: 
    print("Gano", nombre2.lower()) 