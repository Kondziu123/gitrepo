/*
 * tabele1.cpp
 */


#include <iostream>

using namespace std;

void pobierzliczby(int tab[], int ile){
    int i =0;
    for (i = 0; i < ile; i++ ){
        cout << "Podaj liczbe: ";
        cin >> tab[i];
    }
}
void sumuj (int tab[], int ile){
    int i = 0;
    int suma = 0;
    for (i = 0; i < ile; i++){
        suma += tab[i];
        }
        cout << "Sumuj liczby: " << suma << endl;     
}
void najmniejsza int (int tab[], int ile){
    int mini = tab [0];
    for (int i = 0; i < mini; i++){
        if (mini > tab[1])
        mini += tab [1;]
        }
        cout << "najmniejsza liczba: " << mini <endl;
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
    sumuj (liczby, rozmiar);
    najmniejsza (liczby, rozmiar);
    
	return 0;
}

