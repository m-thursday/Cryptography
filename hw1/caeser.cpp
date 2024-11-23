#include "cipher.h"

int main(int argc, char *argv[]){
	if (argc == 4){
		string input = argv[1];
		string message = argv[2];
		int key = stol(argv[3]);
		vector<string> plaintext;
		vector<string> ciphertext;
		
		
		if ((input == "e") || (input == "E")){ //check to see if user is running encryption function
		
			plaintext = handler(message);	
			
			encrypt(plaintext, key);
			
			cout << "The encrypted message is: ";
			for (int j = 0; j < plaintext.size(); j++){ // loops through vector to print out by the character
				cout << plaintext[j] << " ";
			}
			cout << endl;
			
			plaintext.clear(); // clears the vector for new inputs
		}
		
		if ((input == "d") || (input == "D")) { // same as above but for decryption
			
			ciphertext = handler(message);
			
			decrypt(ciphertext, key);
			
			cout << "The decrypted message is: ";
			for (int j = 0; j < ciphertext.size(); j++){
				cout << ciphertext[j] << " ";
			}
			cout << endl;
			
			ciphertext.clear();
		}
	}
	
	else {
		cerr << "Improper amount of arguments provided\n";
		return -1;
	}
	
	return 0;
}
