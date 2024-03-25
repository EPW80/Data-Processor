#include <iostream>
#include <fstream>
int calculate_sum(int a, int b) {return a + b;}
int main() {
    std::ifstream inputFile("input.txt"); 
    int num1, num2;
    if (!inputFile) {
        std::cerr << "Unable to open file" << std::endl;
        return 1;
    }
    inputFile>>num1>>num2;
    inputFile.close();
    int result = calculate_sum(num1, num2);
    std::cout<<"Sum: "<<result<<std::endl;
    return 0;
}

