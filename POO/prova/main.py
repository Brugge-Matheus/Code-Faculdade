import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Perguntas e Respostas")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Fontes
fonte_menu = pygame.font.Font(None, 48)
fonte_pergunta = pygame.font.Font(None, 36)
fonte_resposta = pygame.font.Font(None, 32)
fonte_tempo = pygame.font.Font(None, 24)
fonte_mensagem = pygame.font.Font(None, 28)
fonte_dica = pygame.font.Font(None, 28)
fonte_opcao = pygame.font.Font(None, 32)

# Perguntas e respostas divididas por categoria
perguntas_por_categoria = {
    "Geral": {
        "Qual é a capital do Brasil?": "Brasília",
        "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
        "Quantos planetas fazem parte do nosso sistema solar?": "Oito",
        "Qual é o maior oceano do mundo?": "Oceano Pacífico",
        "Quem é considerado o pai da filosofia ocidental?": "Sócrates",
        "Quem foi o inventor da lâmpada elétrica?": "Thomas Edison"
    },
    "História": {
        "Quem foi o primeiro presidente dos Estados Unidos?": "George Washington",
        "Quem foi o líder da Revolução Russa de 1917?": "Vladimir Lenin",
        "Qual país construiu a Muralha da China?": "China",
        "Quem foi o imperador romano que incendiou Roma?": "Nero",
        "Qual é o nome da primeira astronauta mulher a viajar para o espaço?": "Valentina Tereshkova",
        "Quem foi o líder militar francês durante a Segunda Guerra Mundial?": "Charles de Gaulle"
    },
    "Ciência": {
        "Quem descobriu a penicilina?": "Alexander Fleming",
        "Qual é o maior órgão do corpo humano?": "Pele",
        "Qual é o elemento mais abundante na crosta terrestre?": "Oxigênio",
        "Qual é a unidade básica de estrutura e função em um organismo?": "Célula",
        "Quem propôs a teoria da relatividade?": "Albert Einstein",
        "Qual é a velocidade da luz no vácuo?": "Aproximadamente 299,792,458 metros por segundo"
    }
}

# Banco de dados de perguntas e respostas
banco_de_perguntas = {
    "Qual é a capital da França?": "Paris",
    "Quem pintou 'A Noite Estrelada'?": "Vincent van Gogh",
    "Qual é a maior lua de Saturno?": "Titã",
    "Quem é o autor de '1984'?": "George Orwell",
    "Quem é o criador da escultura 'O Pensador'?": "Auguste Rodin",
    "Qual é a cidade mais populosa do mundo?": "Tóquio"
}

# Temporizador
tempo_limite = 15  # 15 segundos para responder

# Modo de jogo (0 - Menu, 1 - Singleplayer, 2 - Multiplayer, 3 - Estudo)
modo_jogo = 0

# Variáveis do jogo
pontuacao_por_categoria = {
    "Geral": 0,
    "História": 0,
    "Ciência": 0
}
tempo_inicio = 0

# Estado da mensagem de dica
mostrando_mensagem_dica = False

# Função para mostrar menu inicial
def mostrar_menu():
    tela.fill(branco)
    mostrar_mensagem("Jogo de Perguntas e Respostas", preto, 180)
    mostrar_mensagem("Pressione '1' para Singleplayer", preto, 260)
    mostrar_mensagem("Pressione '2' para Multiplayer", preto, 320)
    mostrar_mensagem("Pressione '3' para Modo de Estudo", preto, 380)
    pygame.display.flip()

# Função para mostrar mensagem na tela
def mostrar_mensagem(texto, cor, y):
    mensagem = fonte_mensagem.render(texto, True, cor)
    tela.blit(mensagem, ((largura - mensagem.get_width()) // 2, y))

# Função para mostrar pergunta na tela
def mostrar_pergunta(pergunta):
    texto_pergunta = fonte_pergunta.render(pergunta, True, preto)
    tela.blit(texto_pergunta, (20, 50))

# Função para mostrar resposta na tela
def mostrar_resposta(resposta, y):
    texto_resposta = fonte_resposta.render(resposta, True, preto)
    tela.blit(texto_resposta, (20, y))

# Função para mostrar temporizador na tela
def mostrar_temporizador(tempo_restante):
    global mostrando_mensagem_dica
    texto_tempo = fonte_tempo.render(f"Tempo restante: {int(tempo_restante)}", True, preto)
    tela.blit(texto_tempo, (20, altura - 50))

    # Mostra a mensagem de dica sempre
    mostrar_mensagem("Pressione ',' para obter uma dica!", preto, altura - 80)

# Função para mostrar pontuação na tela
def mostrar_pontuacao():
    y = 20
    for categoria, pontuacao in pontuacao_por_categoria.items():
        texto_pontuacao = fonte_tempo.render(f"{categoria}: {pontuacao} pontos", True, preto)
        tela.blit(texto_pontuacao, (20, y))
        y += 30

# Função para mostrar dica na tela
def mostrar_dica(dica):
    if dica:
        texto_dica = fonte_dica.render(dica, True, preto)
        tela.blit(texto_dica, (20, 200))  # Ajuste na posição vertical

# Função para selecionar uma pergunta aleatória de uma categoria específica
def selecionar_pergunta(categoria):
    if categoria in perguntas_por_categoria:
        perguntas = list(perguntas_por_categoria[categoria].items())
        return random.choice(perguntas)
    return None, None

# Função para selecionar uma pergunta aleatória do banco de perguntas geral
def selecionar_pergunta_geral():
    return random.choice(list(banco_de_perguntas.items()))

# Função principal do jogo - Singleplayer
def jogo_singleplayer():
    global tempo_inicio, mostrando_mensagem_dica

    rodando = True
    while rodando:
        tela.fill(branco)

        categoria = escolher_categoria()
        perguntas_respondidas = set()  # Conjunto para controlar perguntas já feitas
        mostrando_mensagem_dica = False  # Reinicia o estado da mensagem de dica
        while len(perguntas_respondidas) < len(perguntas_por_categoria[categoria]):
            pergunta, resposta = selecionar_pergunta(categoria)
            if pergunta not in perguntas_respondidas:
                perguntas_respondidas.add(pergunta)

                mostrar_pergunta(pergunta)
                mostrar_temporizador(tempo_limite)

                pygame.display.flip()

                # Inicializar temporizador
                tempo_inicio = time.time()
                tempo_restante = tempo_limite

                respondido = False
                dica_usada = False
                palpite = ""
                dica = ""  # Inicializa a variável dica aqui

                while tempo_restante > 0 and not respondido:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            rodando = False  # Encerra o loop principal
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_RETURN:
                                if palpite.lower() == resposta.lower():
                                    mostrar_resposta("Resposta correta!", 170)
                                    pygame.display.flip()
                                    pygame.time.wait(1000)  # Aguardar um pouco para ver a resposta
                                else:
                                    mostrar_resposta(f"Resposta incorreta! A resposta correta é: {resposta}", 170)
                                    pygame.display.flip()
                                    pygame.time.wait(1000)  # Aguardar um pouco para ver a resposta
                                respondido = True
                            elif evento.key == pygame.K_BACKSPACE:
                                palpite = palpite[:-1]
                            elif evento.key == pygame.K_COMMA:  # Pressione ',' para uma dica
                                if not dica_usada:
                                    dica = resposta[0] + '_' * (len(resposta) - 1)  # Exibir a primeira letra da resposta
                                    dica_usada = True
                                    mostrando_mensagem_dica = True
                            else:
                                palpite += evento.unicode

                    tela.fill(branco)
                    mostrar_pergunta(pergunta)
                    mostrar_temporizador(tempo_restante)
                    mostrar_resposta(palpite, 120)
                    mostrar_dica(dica)

                    pygame.display.flip()

                    tempo_atual = time.time()
                    tempo_restante = tempo_limite - (tempo_atual - tempo_inicio)

                if not respondido:
                    mostrar_resposta(f"Tempo esgotado! A resposta correta é: {resposta}", 170)
                    pygame.display.flip()
                    pygame.time.wait(1000)  # Aguardar um pouco para ver a resposta

                pygame.time.wait(2000)  # Aguardar um pouco entre as perguntas

        # Exibir pontuação final da categoria
        tela.fill(branco)
        mostrar_pontuacao()
        mostrar_mensagem("Fim do Jogo! Pressione ESC para sair.", preto, 20)
        pygame.display.flip()

        # Aguardar evento para sair
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    esperando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        rodando = False
                        esperando = False

    pygame.quit()  # Encerra o Pygame ao sair do loop principal

# Função para escolher a categoria de perguntas
def escolher_categoria():
    tela.fill(branco)
    mostrar_mensagem("Escolha uma categoria:", preto, 20)
    
    categorias = list(perguntas_por_categoria.keys())
    opcao_y = 100
    opcao_gap = 50
    
    for i, categoria in enumerate(categorias):
        texto_opcao = fonte_opcao.render(f"{i + 1}. {categoria}", True, preto)
        tela.blit(texto_opcao, (150, opcao_y))
        opcao_y += opcao_gap
    
    pygame.display.flip()

    escolhendo = True
    while escolhendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if pygame.K_1 <= evento.key <= pygame.K_3:
                    indice = evento.key - pygame.K_1
                    if 0 <= indice < len(categorias):
                        return categorias[indice]

# Função principal do jogo
def main():
    global modo_jogo
    
    rodando = True
    while rodando:
        mostrar_menu()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    modo_jogo = 1  # Singleplayer
                    jogo_singleplayer()
                elif evento.key == pygame.K_2:
                    modo_jogo = 2  # Multiplayer (ainda não implementado)
                elif evento.key == pygame.K_3:
                    modo_jogo = 3  # Modo de Estudo
                    jogo_singleplayer()

    pygame.quit()  # Encerra o Pygame ao sair do loop principal

if __name__ == "__main__":
    main()
