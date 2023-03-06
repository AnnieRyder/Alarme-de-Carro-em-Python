import random

print("A princípio, o alarme deve disparar apenas se este estiver ligado e uma das portas ser aberta ou se houver alguma movimentação\ndentro do carro para o caso de alguém entrar no carro sem abrir as portas, de algum jeito.")
print("• Temos três informações que nos fornecerão os dados de entrada")
print("■ A: Alarme. 0 para desligado ou 1 para ligado.\n■ B: Porta. 0 para fechada ou 1 para aberta. \n■ C: Movimento: 0 para sem movimento ou 1 para movimento.")

Alarme = random.choice([True, False])
Porta = random.choice([True, False])
Movimento = random.choice([True, False])

print(f"Alarme: {Alarme}, Porta: {Porta}, Movimento: {Movimento}")

valor = (Movimento and Porta and not Alarme) or (Alarme and not Porta and Movimento) or (Alarme and Porta and Movimento)

# Verificando se o alarme dispara ou não
if Alarme:
    print("O alarme disparou!")
elif valor and (Porta or Movimento):
    print("O alarme disparou!")
else:
    print("O alarme não disparou.")
