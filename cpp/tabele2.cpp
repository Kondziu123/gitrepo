/*
 * tabele1.cpp
 */


#include <iostream>

using namespace std;


void ile5(int tab[], int ile){
    int i;
    int licznik5 =0;
    for (int i = 0; i < ile; i++){
        if (tab[i] % 5 == 0)
            licznik5++;
        }
        cout << "ilosc liczb podzielnych przez 5: " << licznik5 << endl;
    }

void pobierzliczby(int tab[], int ile){
    int i =0;
    for (i = 0; i < ile; i++ ){
        cout << "Podaj liczbe: ";
        cin >> tab[i];
    }
}
void najmniejsza (int tab[], int ile){
    int mini = tab [0];
    for (int i = 0; i < mini; i++){
        if (mini > tab[1])
        mini += tab [1];
        }
        cout << "najmniejsza liczba: " << mini << endl;
    ; // funkcja znajduje i drukuje najmniejsza
      // liczba z tabeli
}


int main(int argc, char **argv)
{
    int rozmiar = 0;
    cout << "Ile liczb podasz: ";
    cin >> rozmiar;
    
	int liczby[rozmiar];
    
    pobierzliczby (liczby, rozmiar);
    najmniejsza (liczby, rozmiar);
    ile5 (liczby, rozmiar);
	return 0;
}

