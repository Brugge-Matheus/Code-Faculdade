#include <stdio.h>
#include <locale.h>

int main() {
    char operacao;
    int i, num, resultado;
    
    printf("Escolha a operação desejada:\n +, -, *, ou /: ");
    scanf("%c", &operacao);
    
    printf("Digite um número: ");
    scanf("%d", &num);

    setlocale(LC_NUMERIC, "pt_BR");
    
    switch(operacao) {
        case '+':
             for(i = 1; i <= 10; i++) {
                 resultado = num + i;
                printf("%d + %d = %d\n", num, i, resultado);
            };
            break;
            
        case '-':
             for(i = 1; i <= 10; i++) {
                 resultado = num - i;
                printf("%d - %d = %d\n", num, i, resultado);
            };
            break;
            
        case '*':
             for(i = 1; i <= 10; i++) {
                 resultado = num * i;
                printf("%d x %d = %d\n", num, i, resultado);
            };
            break;
            
        case '/':
             for(i = 1; i <= 10; i++) {
                 resultado = num / i;
                printf("%d / %d = %d\n", num, i, resultado);
            };
            break;
            
        default:
            printf("Operador não encontrado!");
    }
    
    
    return 0;
}
