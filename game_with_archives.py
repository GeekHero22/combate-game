#Problemas / TO DO!!!

#2: Add ITEMS!!!!
#3: At the end of the Battle function, some more comments could be added, as well as in the last game function

#Changed
#1: Dice and attack rolls, if dice is 20 its always max, if its between the minimum then the dmg will be the average between the min and the max
#2: Changed the whole "choose to do max or min attack", because it wasnt asked for. Instead, I used it for defense. Defense uses the acerto maximo, but it will always halve the damage
#3: Added a random name for the game LMAO it's the literal translation of a baldurs gate 3 place ...... You guys can change it
#4: Added A BUNCH of comments, though the portuguese might be dodgy cos i used the translator :P so check it plssss

#Primeiro, importamos o módulo random, que nos permite gerar números aleatórios
import random



#Listas para definir a vida, ataque minimo, ataque máximo, acerto minimo e acerto máximo do guerreiro, do mago e do ladino
guerreiro = [60, 7, 14, 6, 12]
mago = [40, 9, 18, 7, 15]
ladino = [30, 8, 20, 7, 15]
itens = ["anel de força", "poção de cura"]

#Colocamos todas as classes como uma sublista na lista de classes
classes = [guerreiro, mago, ladino]

#Variáveis ​vazias ​de vida e stats (estatísticas) de ambos os jogadores
vida_jogador1 = 0
vida_jogador2 = 0
stats_jogador1 = []
stats_jogador2 = []
boost = 0
nome_jogador1 = ""
nome_jogador2 = ""

#Função que permite que ambos os jogadores escolham sua classe
def escolher_clase(jogador):
    #Mensagem de boas-vindas, que também informa as turmas
    print("Bem-vindo ao jogo: 'Encontro das Sombras'! Guerreiros, Magos e Ladinos esperam por você.")
    print("A aventura começa! Primeiro, escolha sua classe: 1 para ser Guerreiro, 2 para Mago ou 3 para Ladino.")

    #Com "global" fazemos com que as variáveis ​​possam ser usadas
    global classes, stats_jogador1, stats_jogador2

    #Inicio de um loop "while", o programa continua perguntando até que o jogador escolha um número de classe válido\
    while True:
        #Variável de escolha criada, para que o jogador escolha sua classe
        escolha = int(input(f"Escolha sua classe {jogador}! "))

        if escolha in [1, 2, 3]:
        #Com "if" atribuímos a classe correta (com o índice - 1, então cabe 0, 1, 2), com o jogador determinado
            if jogador == "Jogador 1":
                stats_jogador1 = classes[escolha - 1]

            else:
                stats_jogador2 = classes[escolha - 1]

            print(f"{jogador} escolheu ser um {'Guerreiro' if escolha == 1 else 'Mago' if escolha == 2 else 'Ladino'}.")

            #Para sair do loop se as classes escolhidas estiverem corretas
            break
        
        #Se a entrada for inválida, permite que a classe seja solicitada novamente
        else:
            print("Número inválido, escolha uma classe entre 1, 2 ou 3.")

#função para o nome dos jogares:
# Variáveis para armazenar os nomes dos jogadores
nome_jogador1 = ""
nome_jogador2 = ""

# Função para definir os nomes dos jogadores
def definir_nomes():
    global nome_jogador1, nome_jogador2
    nome_jogador1 = input("Jogador 1, digite seu nome: ")
    nome_jogador2 = input("Jogador 2, digite seu nome: ")
    print(f"Bem-vindos, {nome_jogador1} e {nome_jogador2}! Que comecem os combates!")

# Modificar a função de escolha de classe para usar os nomes
def escolher_clase(jogador):
    print(f"{jogador}, escolha sua classe: 1 para ser Guerreiro, 2 para Mago ou 3 para Ladino.")
    global classes, stats_jogador1, stats_jogador2

    while True:
        escolha = int(input(f"{jogador}, escolha sua classe: "))
        if escolha in [1, 2, 3]:
            if jogador == nome_jogador1:
                stats_jogador1 = classes[escolha - 1]
            else:
                stats_jogador2 = classes[escolha - 1]
            print(f"{jogador} escolheu ser um {'Guerreiro' if escolha == 1 else 'Mago' if escolha == 2 else 'Ladino'}.")
            break
        else:
            print("Número inválido, escolha uma classe entre 1, 2 ou 3.")

# Modificar a função de batalha para usar os nomes
def batalha(stats_jogador1, stats_jogador2):
    turno = 0
    vencedor = None

    # Inicializa a vida dos jogadores com base nos stats
    vida_jogador1 = stats_jogador1[0]
    vida_jogador2 = stats_jogador2[0]

    while vida_jogador1 > 0 and vida_jogador2 > 0:
        turno += 1
        print(f"TURNO {turno}.")
        print(f"{nome_jogador1} está com {vida_jogador1} de vida.")
        print(f"{nome_jogador2} está com {vida_jogador2} de vida.")

        defesa_jogador1 = False
        defesa_jogador2 = False

        for jogador, nome in [(1, nome_jogador1), (2, nome_jogador2)]:
            if jogador == 1:
                escolha = int(input(f"{nome}, digite 1 para atacar, 2 para defender ou 3 para usar um item "))
                stats = stats_jogador1
            else:
                escolha = int(input(f"{nome}, digite 1 para atacar, 2 para defender ou 3 para usar um item "))
                stats = stats_jogador2

            # Defesa
            if escolha == 2:
                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {dado}.")
                if dado >= stats[4]:
                    if jogador == 1:
                        defesa_jogador1 = True
                        print(f"{nome} está defendendo! Só receberá metade do dano.")
                    else:
                        defesa_jogador2 = True
                        print(f"{nome} está defendendo! Só receberá metade do dano.")
                else:
                    print(f"{nome} falhou na defesa!")
            
            # Ataque
            elif escolha == 1:
                print(f"{nome} decidiu atacar.")
                dado = random.randint(1, 20)
                print(f"A rolagem do dado resultou em: {dado}.")
                if dado >= stats[3]:
                    dano = (stats[1] + stats[2]) // 2
                    if dado == 20:
                        dano = stats[2]

                    if jogador == 2 and defesa_jogador2:
                        dano = dano / 2
                        print(f"A defesa reduz o dano tomado por {nome_jogador2} pela metade!")
                    elif jogador == 1 and defesa_jogador1:
                        dano = dano / 2
                        print(f"A defesa reduz o dano tomado por {nome_jogador1} pela metade!")

                    if jogador == 1:
                        vida_jogador2 -= dano
                        print(f"{nome_jogador2} recebeu {dano:.2f} de dano e está com {vida_jogador2} de vida!")
                    else:
                        vida_jogador1 -= dano
                        print(f"{nome_jogador1} recebeu {dano:.2f} de dano e está com {vida_jogador1} de vida!")
                else:
                    print(f"Ataque de {nome} errou! Nenhum dano foi causado.")
            
            # Uso de item
            elif escolha == 3:
                print(f"{nome} decidiu utilizar um item, digite 1 para o anel de força, ou 2 para poção de vida.")
                escolha_item = int(input())
                if escolha_item == 2:
                    if jogador == 1:
                        vida_jogador1 += 10
                        print(f"{nome} foi curado, sua vida atual agora é: {vida_jogador1}")
                    else:
                        vida_jogador2 += 10
                        print(f"{nome} foi curado, sua vida atual agora é: {vida_jogador2}")
                elif escolha_item == 1:
                    print(f"{nome} usou o anel de força! (ainda não implementado)")
                else:
                    print("Escolha inválida para item.")
    
    if vida_jogador1 <= 0:
        print(f"{nome_jogador2} venceu!")
        vencedor = nome_jogador2
    elif vida_jogador2 <= 0:
        print(f"{nome_jogador1} venceu!")
        vencedor = nome_jogador1

    print("Obrigado por jogar 'Encontro das Sombras'! Esperamos que tenha se divertido!")
    return vencedor

# Função do jogo final
def jogo():
    definir_nomes()  # Solicita os nomes antes do combate
    escolher_clase(nome_jogador1)
    escolher_clase(nome_jogador2)
    vencedor = batalha(stats_jogador1, stats_jogador2)
    return vencedor

# Usando a função para iniciar o jogo
vencedor = jogo()
print(f"O vencedor é: {vencedor}")

with open("log.txt", "w") as log:
    log.write(vencedor)
