/*
 * sewera_ulamek.cpp
 */


#include <iostream>

using namespace std;


int skruc(int licznik; int mianownik)
    int i = 0;
    for (i = mianownik; i > 1; i--){
        if (licznik % i == 0){

        if (mianownik % i == 0){

        licznik=licznik/i;
        mianownik=mianownik/i;
}
}
}
int main(int argc, char **argv)
{
    cout << "Podaj licznik: ";
    cin >> licznik;
    cout << "Podaj mianownik: ";
    cin >> mianownik;

    cout << "Ułamek po skroceniu wynosi: " << licznik << " / " << mianownik << endl;

	return 0;
}
