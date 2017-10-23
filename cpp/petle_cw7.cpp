/*
 * petle_cw7.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int m =0;
	for (i=1; i<3; i++)
    {
        cout << "Podaj numer miesiaca: ";
        cin >> m;
        if (m > 0 && m< 12) break;
        else cout << "Błedne dane!" << endl;
       
            }
	return 0;
}

