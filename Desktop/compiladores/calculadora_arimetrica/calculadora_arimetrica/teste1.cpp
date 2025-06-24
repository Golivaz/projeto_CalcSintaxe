#include <iostream> // Inclui a biblioteca para std::cout

int main() {
    int x;
    float y;

    x = 10.6;
    y = 5.5 + x * 2.0; // Testando expressões

    if (x > 5) {
        print(x);
    } else {
        print(y);
    }

    while (x < 15) {
        x = x + 1;
        print(x);
    }
}

int outraFuncao() {
    int z;
    z = 100;
    print(z);
}