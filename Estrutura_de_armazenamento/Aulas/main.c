#include <stdio.h>

int main() {
    int i, num1, num2, soma = 0;
    
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    
    printf("Digite o segundo número: ");
    scanf("%d", &num2);
    
    for (i = num1; i <= num2; i++) {
        soma += i;
    }
    
    printf("A soma entre %d e %d é %d",num1, num2, soma);

    return 0;
}
