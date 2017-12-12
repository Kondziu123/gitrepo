/*
 * Sewera_lokata.py
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int suma, ile, wplata;
    cout << "Wprowadz ilosc wplat: ";
    cin >> ile;
    wplata = 100;
    suma = 0;
    int i;
    for(i =0; i<ile; i++) {
        suma += wplata;
    wplata +=  10;
}
    cout << "Ostatnia wplata wyniosla: " << wplata-10;
    scout << "Stan konta: " << suma << "\n"; 
	return 0;
}

