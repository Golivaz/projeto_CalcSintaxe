
// Função principal que não faz muito, apenas para iniciar.
int main() {
    print(1); // Um comando simples.
}

// Função para calcular o fatorial de um número (fixo)
// Testa laços, condicionais aninhadas e múltiplas declarações.
int calcularFatorial() {
    int n, i, resultado; // Teste de declaração múltipla com vírgula

    n = 6; // Número para o qual calcularemos o fatorial
    i = 1;
    resultado = 1;

    print(n); // Imprime o valor inicial a ser calculado

    while (i <= n) {
        resultado = resultado * i;

        // Teste de um IF aninhado dentro do WHILE
        if (resultado > 100) {
            print(resultado);
        }

        i = i + 1;
    }
}

// Função para testar um bloco de código vazio.
int funcaoVazia() {
    
}