/*
 * sumuj2.cpp
 * Program pobiera liczby od urzytkownika aż ich suma przekroczy 100.
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	// int i;
    int suma = 0;
    int liczba = 0;
    int ilosc_liczb = 0;
    cout << "Podaj ilość liczb: " << endl;
    cout << "Wprowadzaj kolejne liczby: " <<endl;
    // for (;;)
    while (1)
    {
        cin >> liczba;
        ilosc_liczb++;
        cout << "Podano: " << liczba << endl;
        suma += liczba;
        
        if (suma > 100)
            break;
    
    };
    cout << "Suma liczb: " << suma << endl;
    cout << "Wprowadż liczb: " << ilosc_liczb << endl; 
    
        
	return 0;
}

