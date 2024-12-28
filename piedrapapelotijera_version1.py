jugador1= input("Hola Jugador 1, ¿qué eliges: Piedra, Papel o Tijera?: ")
jugador2= input("Hola Jugador 2, ¿qué eliges: Piedra, Papel o Tijera?: ")


if jugador1 == jugador2:
        print("Ha sigo un empate")
elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Papel" and jugador2 == "Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
        print("Gano jugador 1")
else: 
        print("Gano jugador 2") 