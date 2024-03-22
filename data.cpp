#include <iostream>
#include <fstream> // Include for file handling

// Function to calculate the sum of two integers
int calculate_sum(int a, int b) {
    // This function calculates the sum of two numbers
    return a + b;
}

// Main function
int main() {
    std::ifstream inputFile("input.txt"); // Open input file
    int num1, num2;

    if (!inputFile) { // Check if the file was successfully opened
        std::cerr << "Unable to open file" << std::endl;
        return 1; // Return an error code
    }

    // input.txt contains two integers separated by space
    inputFile >> num1 >> num2;
    inputFile.close(); // Close the file

    // Calculate the sum
    int result = calculate_sum(num1, num2);

    // Print the result
    std::cout << "Sum: " << result << std::endl;

    return 0;
}
