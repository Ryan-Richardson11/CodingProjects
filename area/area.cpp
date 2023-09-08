#include <iostream>

using namespace std;

void calculateArea(int length, int width){
    int area;
    area = length * width;
    cout << "The area of the rectangle is " << area << endl;
}

int main(){
    int length;
    int width;
    cout << "Please enter the rectangles length: ";
    cin >> length;
    cout << "Please enter the rectangles width: ";
    cin >> width;
    calculateArea(length, width);
    return 0;
}
