#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

#define PONTUACAO_MAXIMA 10

typedef struct {
    int min;
    int max;
    int max_tentativas;
} Intervalo;

#define NIVEIS_DIFICULDADE 3

typedef enum {
    JOGANDO,
    GANHOU,
    PERDEU
} EstadoJogo; // Declaração da enumeração EstadoJogo

Intervalo obterIntervaloDificuldade(int nivel) {
    Intervalo intervalo;
    switch (nivel) {
        case 1: // Fácil
            intervalo.min = 1;
            intervalo.max = 50;
            intervalo.max_tentativas = 15; // Defina o número de tentativas para o nível fácil
            break;
        case 2: // Médio
            intervalo.min = 1;
            intervalo.max = 100;
            intervalo.max_tentativas = 10; // Defina o número de tentativas para o nível médio
            break;
        case 3: // Difícil
            intervalo.min = 1;
            intervalo.max = 200;
            intervalo.max_tentativas = 5; // Defina o número de tentativas para o nível difícil
            break;
        default: // Nível inválido
            intervalo.min = 1;
            intervalo.max = 100;
            intervalo.max_tentativas = 10; // Padrão
            break;
    }
    return intervalo;
}

int gerarNumeroSecreto(int min, int max) {
    return rand() % (max - min + 1) + min;
}

int validarPalpite(char *entrada, Intervalo intervalo) {
    int palpite = atoi(entrada);
    if (palpite < intervalo.min || palpite > intervalo.max) {
        printf("Por favor, insira um numero dentro do intervalo fornecido.\n");
        return 0; // Palpite inválido
    }
    return 1; // Palpite válido
}

void imprimirMensagem(char *mensagem) {
    printf("%s\n", mensagem);
}

void exibirInstrucoes() {
    printf("=== Instruções ===\n");
    printf("Você deve adivinhar o numero secreto.\n");
    printf("O numero está dentro de um intervalo específico, dependendo do nível de dificuldade escolhido.\n");
    printf("Você tem um numero limitado de tentativas para acertar o numero secreto.\n");
    printf("Após cada tentativa, será informado se o palpite está muito alto ou muito baixo.\n");
    printf("Boa sorte!\n");
}

EstadoJogo jogarJogo() {
    srand(time(NULL));
    int nivel;
    printf("Escolha o nível de dificuldade:\n");
    printf("1. Fácil\n");
    printf("2. Médio\n");
    printf("3. Difícil\n");
    printf("Digite o numero do nível: ");

    if (scanf("%d", &nivel) != 1) {
        printf("Erro de entrada. Certifique-se de digitar um numero.\n");
        return PERDEU; // Saída com erro
    }
    getchar(); // Limpar o buffer de entrada

    Intervalo intervalo = obterIntervaloDificuldade(nivel);
    int numeroSecreto = gerarNumeroSecreto(intervalo.min, intervalo.max);
    int palpite;
    char entrada[100];
    int tentativas = 0;

    while (tentativas < intervalo.max_tentativas) {
        printf("Tentativa %d de %d. Adivinhe o numero secreto (entre %d e %d): ", tentativas + 1, intervalo.max_tentativas, intervalo.min, intervalo.max);
        if (fgets(entrada, sizeof(entrada), stdin) == NULL) {
            printf("Erro de entrada. Não foi possível ler a entrada.\n");
            return PERDEU; // Saída com erro
        }

        if (!validarPalpite(entrada, intervalo)) {
            continue;
        }

        palpite = atoi(entrada);
        
        if (palpite < numeroSecreto) {
            imprimirMensagem("Muito baixo! Tente um numero maior.");
        } else if (palpite > numeroSecreto) {
            imprimirMensagem("Muito alto! Tente um numero menor.");
        } else {
            int pontuacao = PONTUACAO_MAXIMA / (tentativas + 1);
            printf("Parabéns! Você acertou o numero secreto em %d tentativa(s). Sua pontuação é: %d.\n", tentativas + 1, pontuacao);
            return GANHOU; // Sucesso
        }
        
        tentativas++;
    }

    if (tentativas == intervalo.max_tentativas) {
        printf("Você excedeu o limite de tentativas. O numero secreto era %d.\n", numeroSecreto);
    }

    return PERDEU; // Perdeu após exceder as tentativas
}

int main() {
    int opcao;
    EstadoJogo estado;

    do {
        printf("\n=== Menu ===\n");
        printf("1. Iniciar Novo Jogo\n");
        printf("2. Ver Instruções\n");
        printf("3. Sair\n");
        printf("Escolha uma opção: ");

        if (scanf("%d", &opcao) != 1) {
            printf("Erro de entrada. Certifique-se de digitar um numero.\n");
            return 1; // Saída com erro
        }
        getchar(); // Limpar o buffer de entrada

        switch (opcao) {
            case 1:
                estado = jogarJogo();
                if (estado == PERDEU) {
                    printf("Você perdeu! Tente novamente.\n");
                }
                break;
            case 2:
                exibirInstrucoes();
                break;
            case 3:
                printf("Saindo do jogo...\n");
                break;
            default:
                printf("Opção inválida. Por favor, escolha uma opção válida.\n");
                break;
        }
    } while (opcao != 3);

    return 0;
}
