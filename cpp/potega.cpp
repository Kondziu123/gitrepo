/*
 * potega.cpp
 * a0 = 1
 * a1 = a 
 * an = a*....*a (n - czynników) dla n zaw. N+ - {1} 
 */


#include <iostream>


using namespace std;

float potega_it(float x, int n) {
    float wynik = 1;
    for(int i = 0; i < n; i++) {
        cout << i << endl;
        wynik = wynik * x;
    }
    return wynik;    
} 

int potega_rek(int a,int n);
    if n == 0
        return 1;
    return potega_rek(a, n - 1) * a; 

int main(int argc, char **argv)
{
    float x= 0;
    int n = 0;
	//pobierz od użytkownika podstawę i wykładnik
    cout << "Podstawa: " << endl;
    cin >> x;
    cout << "Wykładnik: " << endl;
    cin >> n;
    cout << "Potęga: " << potega_it(x, n) << endl;
	return 0;
}

