#include <iostream>
#include <math.h>
using namespace std;
int main() {
	int i = 0;
	cout << "i is " << i << endl;
	i = i + 1;
	cout << "now i is " << i << endl;
	float a = 2.3999999999999999999;
	cout << "a is " << a << endl;
	double b = 3.5999999999999999999999;
	cout << "b is " << b << endl;

	i = 5;
	int j = i/2;
	cout << j << endl;

	a = 5;
	double c = a/2;
	cout << "c is " << c << endl;

	double answer;
	cout << "please type answer " << endl;
	cin >> answer;
	cout << "your answer is " << answer << endl;

	if (answer >= 0) {
		float e = sqrt(answer);
		cout << "sqrt of answer is " << e << endl;
	} else {
		cout << "no real answer try again buddy" << endl;
	}
}

