#include <stdio.h>
#include <locale.h>

int main() {
    char operacao;
    float num1, num2, resultado;
    
    printf("Escolha a operação desejada:\n +, -, *, ou /: ");
    scanf("%c", &operacao);
    
    printf("Digite o primeiro número: ");
    scanf("%f", &num1);
    
    printf("Digite o segundo número: ");
    scanf("%f", &num2);

    setlocale(LC_NUMERIC, "pt_BR");
    
    switch(operacao) {
        case '+':
            resultado = num1 + num2;
            printf("O resultado de %.1f + %.1f é = %.1f", num1, num2, resultado);
            break;
        
        case '-':
           resultado = num1 - num2;
            printf("O resultado de  %.1f - %.1f é = %.1f", num1, num2, resultado);
            break;
            
        case '*':
           resultado = num1 * num2;
            printf("O resultado de  %.1f * %.1f é = %.1f", num1, num2, resultado);
            break;
            
        case '/':
           resultado = num1 / num2;
            printf("O resultado de  %.1f / %.1f é = %.1f", num1, num2, resultado);
            break;
            
        default:
            printf("Não foi identificado o operador");
        
    }
    
    
    return 0;
}
