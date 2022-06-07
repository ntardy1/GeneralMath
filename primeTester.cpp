#include <iostream>
#include <vector>


void printVector(std::vector<int> vector){
    for (int i = 0; i < vector.size(); i++){
        std::cout << vector[i] << "\n";
    }
}

int main(){
    // Declaring Variables
    int number;
    std::vector<int> factors;
    // Getting the number to be tested
    std::cout << "Number: ";
    std::cin >> number;
    // Checking every possible factor of the number
    for (int i = 1; i <= number; i++){
        if (number % i == 0){
            factors.push_back(i);
        }
    }
    // If the number is prime, its only factors will be 1 and itself
    if (factors.size() == 1 or factors.size() == 2){
        std::cout << "Prime";
    // If the number has more than 2 factors, then it is composite
    } else {
        std::cout << "Composite" << "\n";
    }
    std::cout << "Factors: " << "\n";
    printVector(factors); 
}