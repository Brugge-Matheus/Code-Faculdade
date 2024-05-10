import random
import threading
import time

# Banco de dados de perguntas por níveis de dificuldade e categorias
banco_de_perguntas = {
    "facil": {
        "entretenimento": {
            "abertas": {
                "Quanto é 2 + 2?": ("4", "Adição simples..."),
                "Quem foi o primeiro presidente do Brasil?": ("Deodoro da Fonseca", "Deodoro..."),
            },
            "multipla_escolha": {
                "Qual é a capital da França?": (["a) Paris", "b) Roma", "c) Londres", "a"], "Cidade do amor..."),
                "Qual é o maior oceano do mundo?": (["a) Atlântico", "b) Índico", "c) Pacífico", "c"], "Maior oceano..."),
            },
        },
        "biologia": {
            "abertas": {
                "Qual é a raiz quadrada de 144?": ("12", "Número..."),
                "Qual é a fórmula química da água?": ("H2O", "Duas letras..."),
            },
            "multipla_escolha": {
                "Quem descobriu a penicilina?": (["a) Alexander Fleming", "b) Albert Einstein", "c) Isaac Newton", "a"], "Iniciou a era dos antibióticos..."),
                "Quem foi o primeiro astronauta a pisar na Lua?": (["a) Buzz Aldrin", "b) Neil Armstrong", "c) Yuri Gagarin", "b"], "Passo gigante..."),
            },
        },
    },
    "medio": {
        "entretenimento": {
            "abertas": {
                "Quem escreveu 'Dom Quixote'?": ("Miguel de Cervantes", "Miguel..."),
                "Quem pintou a Mona Lisa?": ("Leonardo da Vinci", "Leonardo..."),
            },
            "multipla_escolha": {
                "Quantos planetas fazem parte do nosso sistema solar?": (["a) Sete", "b) Nove", "c) Oito", "c"], "Menos de dez"),
                "Qual é o maior animal terrestre?": (["a) Baleia Azul", "b) Elefante Africano", "c) Girafa", "b"], "O maior mamífero..."),
            },
        },
        "biologia": {
            "abertas": {
                "Qual é o órgão responsável pela produção de insulina no corpo humano?": ("Pâncreas", "Pâncreas..."),
                "Quantas câmaras possui o coração humano?": ("Quatro", "Quatro..."),
            },
            "multipla_escolha": {
                "Qual destes animais não é um mamífero?": (["a) Golfinho", "b) Tubarão", "c) Elefante", "b"], "Peixe cartilaginoso..."),
                "Qual destes é considerado o menor osso do corpo humano?": (["a) Estribo", "b) Fêmur", "c) Úmero", "a"], "Ossículo..."),
            },
        },
    },
    "dificil": {
        "entretenimento": {
            "abertas": {
                "Quem é o criador da série de livros 'Harry Potter'?": ("J.K. Rowling", "J.K. Rowling..."),
                "Qual é o nome do primeiro filme da saga 'Star Wars'?": ("Star Wars: Episódio IV - Uma Nova Esperança", "Episódio IV..."),
            },
            "multipla_escolha": {
                "Qual é o sobrenome da família protagonista da série 'Os Simpsons'?": (["a) Simpson", "b) Smith", "c) Cooper", "a"], "A família..."),
                "Quem interpretou o personagem Jack em 'Titanic'?": (["a) Leonardo DiCaprio", "b) Tom Cruise", "c) Brad Pitt", "a"], "Rei do mundo..."),
            },
        },
        "biologia": {
            "abertas": {
                "Qual é a função das mitocôndrias dentro da célula?": ("Produção de energia", "Produção de ATP..."),
                "Qual é o nome do processo de divisão celular onde uma célula se divide em duas células filhas idênticas?": ("Mitose", "Mitose..."),
            },
            "multipla_escolha": {
                "Quantos cromossomos possui um ser humano normal?": (["a) 46", "b) 23", "c) 48", "a"], "Número..."),
                "Qual é o nome do processo de formação de gametas?": (["a) Mitose", "b) Meiose", "c) Clivagem", "b"], "Divisão reducional..."),
            },
        },
    },
}

# Função para mostrar uma pergunta com o opção de usar uma pista
def mostrar_pergunta(pergunta, resposta, pista):
    print(pergunta)
    print(f"Dica: {pista}")
    inicio = time.time()  # Captura o tempo de início
    palpite = input("Sua resposta: ").strip().lower()
    fim = time.time()  # Captura o tempo de fim
    tempo_resposta = round(fim - inicio, 2)  # Calcula o tempo de resposta e arredonda para 2 casas decimais

    if palpite == resposta.lower():
        pontuacao = 1  # Pontuação base
        if tempo_resposta < 20:  # Alteração do tempo limite para 20 segundos
            pontuacao += 2
            print(f"Resposta correta! Você ganhou 2 pontos extras por ser rápido.")
        else:  # Se demorar mais de 20 segundos, ganha apenas 1 ponto extra
            pontuacao += 1
            print("Resposta correta!")
    else:
        pontuacao = -1  # Pontuação base
        print(f"Incorreto! A resposta correta é '{resposta}'.")

    return pontuacao

# Função para mostrar uma pergunta de múltipla escolha com o opção de usar uma pista
def mostrar_pergunta_multipla_escolha(pergunta, opcoes, resposta, pista):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    print(f"Dica: {pista}")
    inicio = time.time()  # Captura o tempo de início
    palpite = input("Sua resposta: ").strip().lower()
    fim = time.time()  # Captura o tempo de fim
    tempo_resposta = round(fim - inicio, 2)  # Calcula o tempo de resposta e arredonda para 2 casas decimais

    if palpite == resposta.lower():
        pontuacao = 1  # Pontuação base
        if tempo_resposta < 20:  # Alteração do tempo limite para 20 segundos
            pontuacao += 2
            print(f"Resposta correta! Você ganhou 2 pontos extras por ser rápido.")
        else:  # Se demorar mais de 20 segundos, ganha apenas 1 ponto extra
            pontuacao += 1
            print("Resposta correta!")
    else:
        pontuacao = -1  # Pontuação base
        print(f"Incorreto! A resposta correta é '{resposta}'.")

    return pontuacao


# Função para mostrar uma pergunta de múltipla escolha com a opção de usar uma pista
def mostrar_pergunta_multipla_escolha(pergunta, opcoes, resposta, pista):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    print(f"Dica: {pista}")
    inicio = time.time()  # Captura o tempo de início
    palpite = input("Sua resposta: ").strip().lower()
    fim = time.time()  # Captura o tempo de fim
    tempo_resposta = round(fim - inicio, 2)  # Calcula o tempo de resposta e arredonda para 2 casas decimais

    if palpite == resposta.lower():
        pontuacao = 1  # Pontuação base
        if tempo_resposta < 5:  # Se responder em menos de 5 segundos, ganha 2 pontos extras
            pontuacao += 2
            print(f"Resposta correta! Você ganhou 2 pontos extras por ser rápido.")
        else:  # Se demorar mais de 5 segundos, ganha apenas 1 ponto extra
            pontuacao += 1
            print("Resposta correta!")
    else:
        pontuacao = -1  # Pontuação base
        print(f"Incorreto! A resposta correta é '{resposta}'.")

    return pontuacao

# Função para definir o temporizador
def temporizador():
    print("\nTempo esgotado!")

# Função para o novo modo de jogo dinâmico
def modo_jogo_dinamico():
    print("Bem-vindo ao novo modo de jogo dinâmico!\n")
    print("Este modo de jogo começa com perguntas de dificuldade fácil.")
    print("Se você acertar todas as perguntas, avançará para a dificuldade média.")
    print("Acertando todas as perguntas de médio, avançará para a dificuldade difícil.")
    print("Se errar alguma pergunta, o jogo terminará e sua pontuação será exibida.\n")

    nivel_dificuldade = "facil"  # Começa com o nível de dificuldade fácil
    pontuacao_total = 0  # Inicializa a pontuação total

    while nivel_dificuldade in banco_de_perguntas.keys():
        print(f"Perguntas do nível de dificuldade: {nivel_dificuldade.capitalize()}\n")
        perguntas_selecionadas = []

        for categoria, tipos in banco_de_perguntas[nivel_dificuldade].items():
            for tipo, perguntas in tipos.items():
                for pergunta, (resposta, pista) in perguntas.items():
                    perguntas_selecionadas.append((pergunta, resposta, pista))

        random.shuffle(perguntas_selecionadas)  # Embaralha as perguntas

        todas_corretas = True
        for pergunta, resposta, pista in perguntas_selecionadas:
            if type(resposta) == list:  # Pergunta de múltipla escolha
                print("\nVocê tem 20 segundos para responder a esta pergunta:")
                temporizador_thread = threading.Timer(20, temporizador)
                temporizador_thread.start()

                pontuacao = mostrar_pergunta_multipla_escolha(pergunta, resposta[:-1], resposta[-1], pista)
                pontuacao_total += pontuacao
                print(f"Você ganhou {pontuacao} pontos nesta pergunta.\n")  

                temporizador_thread.cancel()
            else:  # Pergunta aberta
                print("\nVocê tem 20 segundos para responder a esta pergunta:")
                temporizador_thread = threading.Timer(20, temporizador)
                temporizador_thread.start()

                pontuacao = mostrar_pergunta(pergunta, resposta, pista)
                pontuacao_total += pontuacao
                print(f"Você ganhou {pontuacao} pontos nesta pergunta.\n")  

                temporizador_thread.cancel()

            if pontuacao == -1:  # Se o jogador errar, o jogo termina
                todas_corretas = False
                break

        if todas_corretas:
            if nivel_dificuldade == "facil":
                nivel_dificuldade = "medio"
                print("Parabéns! Você acertou todas as perguntas do nível fácil.\n"
                      "Avançando para o nível médio...\n")
            elif nivel_dificuldade == "medio":
                nivel_dificuldade = "dificil"
                print("Parabéns! Você acertou todas as perguntas do nível médio.\n"
                      "Avançando para o nível difícil...\n")
            else:
                print("Parabéns! Você acertou todas as perguntas do nível difícil.\n"
                      "Fim do jogo.")
                break
        else:
            print("Fim do jogo.")
            break

    print(f"\nSua pontuação final é: {pontuacao_total} pontos.")

# Função para o modo single player
def modo_singleplayer():
    print("Bem-vindo ao modo single player!")
    nivel_dificuldade = input("Escolha o nível de dificuldade: (facil / medio / dificil): ").strip().lower()

    if nivel_dificuldade not in banco_de_perguntas.keys():
        print("Nível de dificuldade inválido. Por favor, escolha entre 'facil', 'medio' ou 'dificil'.")
        return

    print("\nEscolha a categoria:")
    categorias_disponiveis = list(banco_de_perguntas[nivel_dificuldade].keys())
    for i, categoria in enumerate(categorias_disponiveis, start=1):
        print(f"{i}. {categoria.capitalize()}")

    categoria_escolhida = int(input("Opção: ")) - 1

    if categoria_escolhida not in range(len(categorias_disponiveis)):
        print("Categoria inválida.")
        return

    print("\nVamos começar...\n")
    perguntas_selecionadas = []

    for tipo_pergunta, perguntas in banco_de_perguntas[nivel_dificuldade][categorias_disponiveis[categoria_escolhida]].items():
        for pergunta, (resposta, pista) in perguntas.items():
            perguntas_selecionadas.append((pergunta, resposta, pista))

    random.shuffle(perguntas_selecionadas)  # Embaralha as perguntas

    pontuacao_total = 0.0  # Altera para ponto flutuante

    for pergunta, resposta, pista in perguntas_selecionadas:
        if type(resposta) == list:  # Pergunta de múltipla escolha
            print("\nVocê tem 20 segundos para responder a esta pergunta:")
            temporizador_thread = threading.Timer(20, temporizador)
            temporizador_thread.start()

            pontuacao = mostrar_pergunta_multipla_escolha(pergunta, resposta[:-1], resposta[-1], pista)
            pontuacao_total += pontuacao
            print(f"Você ganhou {pontuacao:.2f} pontos nesta pergunta.")  

            temporizador_thread.cancel()
        else:  # Pergunta aberta
            print("\nVocê tem 20 segundos para responder a esta pergunta:")
            temporizador_thread = threading.Timer(20, temporizador)
            temporizador_thread.start()

            pontuacao = mostrar_pergunta(pergunta, resposta, pista)
            pontuacao_total += pontuacao
            print(f"Você ganhou {pontuacao:.2f} pontos nesta pergunta.")  

            temporizador_thread.cancel()

    print(f"\nSua pontuação final é: {pontuacao_total:.2f}")  

# Função para o modo multiplayer
def modo_multiplayer():
    print("Bem-vindo ao modo multiplayer!")
    num_jogadores = int(input("Quantos jogadores participarão? "))
    jogadores = []

    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores.append({"nome": nome, "pontuacao": 0})

    print("\nVamos começar...\n")

    nivel_dificuldade = input("Escolha o nível de dificuldade: (facil / medio / dificil): ").strip().lower()

    if nivel_dificuldade not in banco_de_perguntas.keys():
        print("Nível de dificuldade inválido. Por favor, escolha entre 'facil', 'medio' ou 'dificil'.")
        return

    print("\nEscolha a categoria:")
    categorias_disponiveis = list(banco_de_perguntas[nivel_dificuldade].keys())
    for i, categoria in enumerate(categorias_disponiveis, start=1):
        print(f"{i}. {categoria.capitalize()}")

    categoria_escolhida = int(input("Opção: ")) - 1

    if categoria_escolhida not in range(len(categorias_disponiveis)):
        print("Categoria inválida.")
        return

    print("\nVamos começar...\n")
    perguntas_selecionadas = []

    for tipo_pergunta, perguntas in banco_de_perguntas[nivel_dificuldade][categorias_disponiveis[categoria_escolhida]].items():
        for pergunta, (resposta, pista) in perguntas.items():
            perguntas_selecionadas.append((pergunta, resposta, pista))

    random.shuffle(perguntas_selecionadas)  # Embaralha as perguntas

    for pergunta, resposta, pista in perguntas_selecionadas:
        print(f"\nPergunta: {pergunta}")
        print(f"Dica: {pista}")

        for jogador in jogadores:
            print(f"\nVez de {jogador['nome']}:")
            if type(resposta) == list:  # Pergunta de múltipla escolha
                pontuacao = mostrar_pergunta_multipla_escolha(pergunta, resposta[:-1], resposta[-1], pista)
            else:  # Pergunta aberta
                pontuacao = mostrar_pergunta(pergunta, resposta, pista)
            jogador['pontuacao'] += pontuacao

    print("\nResultados finais:")
    for jogador in jogadores:
        print(f"{jogador['nome']}: {jogador['pontuacao']} pontos")

# Função para o modo de estudo
def modo_estudo():
    print("Bem-vindo ao modo de estudo!")
    print("Aqui estão as perguntas e respostas por níveis de dificuldade e categorias:\n")
    for nivel, perguntas_nivel in banco_de_perguntas.items():
        print(f"Nível de dificuldade: {nivel.capitalize()}\n")
        for categoria, perguntas_categoria in perguntas_nivel.items():
            print(f"Categoria: {categoria.capitalize()}\n")
            for tipo_pergunta, perguntas in perguntas_categoria.items():
                print(f"Tipo de Pergunta: {tipo_pergunta.capitalize()}\n")
                for pergunta, (resposta, _) in perguntas.items():
                    if type(resposta) == list:
                        print(f"Pergunta: {pergunta}")
                        print(f"Opções: {', '.join(resposta[:-1])}")
                        print(f"Resposta: {resposta[-1]}\n")
                    else:
                        print(f"Pergunta: {pergunta}")
                        resposta_usuario = input("Sua resposta: ").strip().lower()
                        if resposta_usuario == resposta.lower():
                            print("Resposta correta!")
                        else:
                            print(f"Incorreto! A resposta correta é '{resposta}'.\n")

# Função principal para o menu inicial
def main():
    print("Bem-vindo ao Quiz Show!\n")
    print("Escolha o modo de jogo:")
    print("1. Single Player")
    print("2. Multiplayer")
    print("3. Estudo")
    print("4. Modo Dinâmico")

    opcao = input("Opção: ")

    if opcao == "1":
        modo_singleplayer()
    elif opcao == "2":
        modo_multiplayer()
    elif opcao == "3":
        modo_estudo()
    elif opcao == "4":
        modo_jogo_dinamico()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Inicializa o programa
if __name__ == "__main__":
    main()
