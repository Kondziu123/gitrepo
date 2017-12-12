/*
 * sewera_ulamek.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int licznik = 0;
    int mianownik = 0;
    int i = 0;
    cout << "Podaj licznik: ";
    cin >> licznik;
    cout << "Podaj mianownik: ";
    cin >> mianownik;

    for (i = mianownik; i > 1; i--){
        if (licznik % i == 0){

        if (mianownik % i == 0){

        licznik=licznik/i;
        mianownik=mianownik/i;
}
}
}
    cout << "Ułamek po skroceniu wynosi: " << licznik << " / " << mianownik << endl;
	return 0;
}

