/*
 * wejscie_wyjscie.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	char imie[10];
    
    cout << "Podaj imie:";
    cin.getline(imie, 10) ;
    cout << "Cześć, " << imie << endl;
    
    char dzialanie;
    cout <<"Dzialanie?";
    cin >> dzialanie;
    
	return 0;
}

