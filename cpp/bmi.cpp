/*
 * petle_cw1.cpp

 */


#include <iostream>

using namespace std;


int main(int argc, char **argv)
{
    float masa = 0;
    float wzrost = 0;
    float BMI = 0;
        cout << "Podaj mase ciała: " << endl;
        cin >> masa;
        cout << "Podaj wzrost: " << endl;
        cin >> wzrost;
        BMI = masa/(wzrost*wzrost);
        cout << "Twoje BMI wynosi: " << BMI << endl;
        
         
        if(BMI < 18.5)
            cout << "Niedowaga" <<endl;
        else cout << "Norma" << endl;
        
        
	

	return 0;
}

