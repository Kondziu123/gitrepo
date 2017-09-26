/*
 * hello.cpp
 
 */


#include <iostream>

using namespace std;

int main (int argc, char **argv)
{
    int a, b, c;
    a = b = c = 0;
    cout <<"Podaj liczby: " ;
    cin >> a >> b >> c;
    if (a > b) 
    {
        if (a > c) cout << "Największe jest a!";
        else cout << "Najwieksze jest c!";
        
        } 
        {
            ; // a nie jest wieksze od b
            }
    
    
    
    
	return 0;
}

