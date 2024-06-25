#include <iostream>
#include <vector>
#include <algorithm> 

int main() {
    // Defino la lista de enteros
    std::vector<int> list = {2, 4, 6, 8};
    
    // Ordeno la lista de mayor a menor u
    std::sort(list.begin(), list.end(), [](int a, int b) {
        return a > b; 
    });
    
    // Imprimo la lista ordenada
    std::cout << "Vector ordenado de mayor a menor: ";
    for (int num : list) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
