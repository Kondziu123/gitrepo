/*
 * nieparzyste.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj wartość liczby n: ";
    cin >> n;
    for(int i = 1; i < n; i += 2){
        cout << i << " ";
    }
	return 0;
}

