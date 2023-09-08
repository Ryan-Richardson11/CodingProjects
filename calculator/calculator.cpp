#include <iostream>

using namespace std;

double calculator(int a, int b, char op){
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    if (op == '*') return a * b;
    if (op == '/') return a / b;
}

int main(){
    int a;
    int b;
    char op;
    cout << "Enter the value of a: ";
    cin >> a;
    cout << "Enter the operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter the value of b: ";
    cin >> b;
    double ans = calculator(a, b, op);
    cout << "The answer is " << ans << endl;
    return 0;
}