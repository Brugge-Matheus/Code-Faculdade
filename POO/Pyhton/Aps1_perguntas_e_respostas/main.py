import time

def main():
    perguntas_respostas = {
        "Qual é capital do Brasil?": "Brasília",
        "Quem escreveu 'Dom Quixote?'": "Miguel de Cervantes",
        "Quantos planetas fazem parte do nosso sistema solar?": "Oito"
    }

    print("Seja bem vindo ao jogo de perguntas e respostas!")

    pontuacao = 0
    for pergunta, resposta in perguntas_respostas.items():
        print(pergunta)
        palpite = input("Sua resposta: ")
        time.sleep(5)
        print("Deseja ver uma dica?")

        if palpite.lower() == resposta.lower():
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto! A respota correta é '{resposta}'.")

    print(f"Sua pontuação final é: {pontuacao} / {len(perguntas_respostas)}")

if __name__ == "__main__":
    main()