/*
 * algorytm2.cpp
 */


#include <iostream>

using namespace std;


int main(int argc, char **argv)
{
	int n = 0;
    int m = 0;
    int iloczyn = 1;
    int i = 1;
    cout <<"Podaj n: "<< endl;
    cin >> n;
        
    while(i!=1){
        
        cout<<"Podaj m: "<< endl;
        cin >> m;
        iloczyn = iloczyn*m;
        i++;
    }
    cout <<"Wynik:"<<iloczyn<<endl;
    
	return 0;
}

