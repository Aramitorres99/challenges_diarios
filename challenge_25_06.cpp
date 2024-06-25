#include <iostream>
#include <algorithm>

using namespace std; //para evitar escribir std todo el tiempo

int main(){
    string word_user;

    std::cout << "Ingrese una palabra: ";
    //guardo esa palabra en la variable 
    std::cin >> word_user;

    //creo una copia de la palabra
    string reversed_word = word_user;
    //uso la funcion reverse para invertir la copia de la palabra
    reverse(reversed_word.begin(), reversed_word.end());

    //comparo la palabra con la palabra invertida
    if (word_user == reversed_word){
        cout << "La palabra es un palindromo" << endl;

    } else {
        cout << "La palabra no es un palindromo" << endl;
    }

}