
/*
  Este teste testa multiplas funcionalidades do parser de uma vez,
  incluindo reatribuição de variáveis e condições mais complexas.
*/

// Função principal que configura o estado inicial e chama a verificação
int main() {
    int continuar, contador;
    float limite;

    continuar = 1;  // Usa 1 como "true" para o loop
    contador = 0;
    limite = 25.5;

    print(contador);

    // Entra no loop de verificação
    while (continuar == 1) {
        contador = contador + 1;

        // Testa uma condição mais complexa com parênteses e operadores
        if ((contador * 2.5) > limite) {
            
            print(999); // Imprime um "código de parada"
            continuar = 0; // Altera a variável para sair do loop

        } else {
        
            // Apenas imprime o contador se a condição IF for falsa
            print(contador);
        }
    }
}

// Uma segunda função simples para garantir que a análise de múltiplos
int diagnostico() {
    int codigo_final;
    codigo_final = 100;
    print(codigo_final);
}