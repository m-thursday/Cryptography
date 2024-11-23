//Max Thursby || 010967047
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>


using namespace std;

void encrypt(vector<string>& m, int k){
	char l;
	for (int i = 0; i < m.size(); i++){
		for (int j = 0; j < m[i].length(); j++){
			l = m[i][j];
			if(isalpha(l)){
				if (l != ' '){
					if(islower(l)){ // for lower case letters
						l = static_cast<char>(l + k); // modifies the character
						if (l > 'z'){
							l = static_cast<char>(l - 'z' + 'a' - 1); // handles letters going past z
						}
					}
					else{ // for upper case letters
						l = static_cast<char>(l + k);
						if (l > 'Z'){
							l = static_cast<char>(l - 'Z' + 'A' - 1);
						}
					}
				}
			}
			m[i][j] = l; // sets message vector to updated character
		}
	}
}

void decrypt(vector<string>& c, int k){
		char l;
	for (int i = 0; i < c.size(); i++){
		for (int j = 0; j < c[i].length(); j++){
			l = c[i][j];
			if (isalpha(l)){
				if (l != ' '){
					if(islower(l)){ // for lower case letters
						l = static_cast<char>(l - k); // modifies the character
						if (l < 'a'){
							l = static_cast<char>(l + 'z' - 'a' + 1); // handles letters going past z
						}
					}
					else{ // for upper case letters
						l = static_cast<char>(l - k);
						if (l < 'A'){
							l = static_cast<char>(l + 'Z' - 'A' + 1);
						}
					}
				}
			}
			c[i][j] = l; // sets message vector to updated character
		}
	}
}

vector<string> handler(string input){
	vector<string> m;
	
	//cout << "1: " << input << endl;
	
	string temp;
	stringstream s(input);
	
	
	while(s >> temp){ // splits string into individual strings in string vector
		m.push_back(temp);
	}
	
	//cout << "2: ";
	
	for (int i = 0; i < m.size(); i++){
	
		cout << m[i] << " ";
		
	}
	cout << endl;
	
	return m;
	
}
