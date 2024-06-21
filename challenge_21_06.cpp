#include <iostream>

int sumNumber() {
    //defino las variables numero 1 y 2
    int numberOne, numberTwo;

    //le pido al usuario que ingrese un numero
    std::cout << "Ingrese un numero: ";
    //guardo ese numero en la variable 
    std::cin >> numberOne;

    std::cout << "Ingrese otro numero: ";
    std::cin >> numberTwo;
    //sumo los dos numeros
    int sum = numberOne + numberTwo;
    //imprimo la suma de ambos
    std::cout << "La suma de ambos numeros es " << sum << std::endl;
    //retorno la suma
    return sum;
}

int main() {
    //llamo a la funcion sumar numeros
    sumNumber();
    return 0;
}
