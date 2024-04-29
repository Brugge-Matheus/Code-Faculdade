import random
import threading
import sys

palpite = ""
timeout_occurred = False

def main():
    def get_input(timeout):
        global palpite, timeout_occurred
        print(f"Jogador {current_player}: Digite sua resposta:")
        input_thread = threading.Thread(target=input_thread_func)
        input_thread.start()
        input_thread.join(timeout)
        if input_thread.is_alive():
            timeout_occurred = True

    def input_thread_func():
        global palpite
        palpite = input("->")



    dificuldade = ["iniciante", "avançado", "estudo"]

    print("Bem vindo ao jogo de palavras cruzadas!")
    print("Preencha as palavras cruzadas com as respostas corretas.")
    print("Dificulades: inicante / avançado / estudo")
    seldificuldade = input("Digite a dificuldade escolida: ")

    if seldificuldade == "iniciante":
        palavras_cruzadas = [
            "Fruta amarela: _ _ _ _ _ _",
            "Animal domestico: _ _ _ _",
            "Cor primária: _ _ _ _",
            "Peça de roupa usada nos pés _ _ _ _ _",
            "Item utilizado para digitar em um computador _ _ _ _ _ _ _"
        ]

        respostas = ["banana", "gato", "azul", "tenis", "teclado"]
        palavras_respostas = list(zip(palavras_cruzadas, respostas))
        random.shuffle(palavras_respostas)
        palavras_cruzadas, respostas = zip(*palavras_respostas)

    elif seldificuldade == "avançado":
        palavras_cruzadas = [
            "1. Médico do olho: _ _ _ _ _ _ _ _ _ _ _ _ _",
            "2. Ato de parar o carro em uma vaga: _ _ _ _ _ _ _ _ _ _",
            "3. Nome da linguagem usada no código: _ _ _ _ _ _",
            "4. Parque temático localizado na florida: _ _ _ _ _ _",
            "5. Desenho TV animado sobre uma esponja do mar: _ _ _ - _ _ _ _ _ _ _"
        ]
        respostas = ["oftalmologista", "estacionar", "python", "disney", "bob esponja"]
        palavras_respostas = list(zip(palavras_cruzadas, respostas))
        random.shuffle(palavras_respostas)
        palavras_cruzadas, respostas = zip(*palavras_respostas)

    elif seldificuldade == "estudo":

        seldificuldade = input("selecione avançado ou iniciante: ")
        if seldificuldade == "iniciante":
            palavras_cruzadas = [
                "Fruta amarela: _ _ _ _ _ _",
                "Animal domestico: _ _ _ _",
                "Cor primária: _ _ _ _",
                "Peça de roupa usada nos pés _ _ _ _ _",
                "Item utilizado para digitar em um computador _ _ _ _ _ _ _"
            ]

            respostas = ["banana", "gato", "azul", "tenis", "teclado"]
            palavras_respostas = list(zip(palavras_cruzadas, respostas))
            random.shuffle(palavras_respostas)
            palavras_cruzadas, respostas = zip(*palavras_respostas)

        elif seldificuldade == "avançado":
            palavras_cruzadas = [
                "1. Médico do olho: _ _ _ _ _ _ _ _ _ _ _ _ _",
                "2. Ato de parar o carro em uma vaga: _ _ _ _ _ _ _ _ _ _",
                "3. Nome da linguagem usada no código: _ _ _ _ _ _",
                "4. Parque temático localizado na florida: _ _ _ _ _ _",
                "5. Desenho TV animado sobre uma esponja do mar: _ _ _ - _ _ _ _ _ _ _"
            ]
            respostas = ["oftalmologista", "estacionar", "python", "disney", "bob esponja"]
            palavras_respostas = list(zip(palavras_cruzadas, respostas))
            random.shuffle(palavras_respostas)
            palavras_cruzadas, respostas = zip(*palavras_respostas)

        pontuacao = 0
        for i, pista in enumerate(palavras_cruzadas):
            print(pista)
            palpite_estudo = input("Sua resposta: ")

            if palpite_estudo.lower() == respostas[i]:
                print("Correto!")
                pontuacao += 1
            else:
                print(f"Incorreto! A resposta era: '{respostas[i]}'.")
        print(f"Sua pontuação final é: {pontuacao}/{len(palavras_cruzadas)}")
        sys.exit()


    else:
        print("Essa dificuldade não existe.")
        return (seldificuldade)

    jogadores = int(input("Digite o número de jogadores: "))
    players = [f"Jogador {i+1}" for i in range(jogadores)]
    current_player = 0

    pontuacoes = {player: 0 for player in players}

    for i, pista in enumerate(palavras_cruzadas):
        print("\n" + "-"*20)
        print(f"Pista {i+1}:")
        print(pista)
        timeout_occurred = False
        get_input(5)

        if timeout_occurred:
            print("Tempo limite atingido!")
        elif palpite.lower() == respostas[i]:
            print(f"Correto, {players[current_player]}!")
            pontuacoes[players[current_player]] += 1
        else:
            print(f"Incorreto! A resposta correta é '{respostas[i]}'.")

        current_player = (current_player + 1) % len(players)

    print("\n" + "="*20)
    print("Pontuações finais:")
    for player, pontuacao in pontuacoes.items():
        print(f"{player}: {pontuacao}/{len(palavras_cruzadas)}")

if __name__ == "__main__":
    main()