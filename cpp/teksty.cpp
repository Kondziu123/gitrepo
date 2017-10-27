/*
 * teksty.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{   
    int i = 0;
    for (i = 65; i < 91; i++){
        cout << i << " " << char(i) <<endl;
        }
    //char znak = 'a';
    //char znak2 = 'b';
    //cout << znak << " " << int(znak) << endl;
    //cout << znak2 << " " << int(znak2) << endl;
    for (i = 97; i < 123; i++){
        cout << i << " " << char(i) <<endl;
        }
    
    char osoba[25];
    cout << "Podaj imie i nazwisko " << endl;
    //cin >> osoba;
    cin.getline(osoba, 25);
    cout << "Cześć " << osoba << endl;
	
return 0;
}

