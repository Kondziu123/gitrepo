/*
 * rekurencja_5.cpp
 * 
 */


#include <iostream>

using namespace std;
int ciag(int x)
{
        if(x==0)
        return 0;
        else
        return ciag(x-1)+1+(x-1)*2;
}
int main(int argc, char **argv)
{
        int x;
        cout << "ktory wyraz ciagu? ";
        cin >> x;
        cout << ciag(x);
        return EXIT_SUCCESS;
	

}
