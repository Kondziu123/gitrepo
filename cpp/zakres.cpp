/*
 * funkcje2.cpp
 */


#include <iostream>

using namespace std;

// int liczba, krok; // zmienne globalne

int zwieksz(int a, int b) {
    a= a + b;
    b = 3 * b;
    return b; 
}

void zwieksz2(int &a, int&b){

        a = a + b;
        b = 3 * b;
}

int main(int argc, char **argv)
{
    int liczba, krok; // zmienne lokalne
    cout << "Podaj liczbe i krok: ";
    cin >> liczba >> krok;
    
    
    
    cout << "Liczba i krok: " << liczba << " " << &liczba<< endl;
    // zwieksz();

    /*
    zwieksz2(liczba, krok);
    cout << "Liczba i krok: "<< liczba << " " << krok << endl;
    */    
	return 0;
}

