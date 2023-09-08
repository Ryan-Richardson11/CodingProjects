#include <iostream>

using namespace std;

void fahrenheitToCelsius(int f){
    int celsius;
    celsius = (f - 32) * 5/9;
    cout << "The temperature is " << celsius << " celsius"<< endl;
}

int main(){
    int f;
    cout << "Enter the temperature in fahrenheit: ";
    cin >> f;
    fahrenheitToCelsius(f);
    return 0;
}