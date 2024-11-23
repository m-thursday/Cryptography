#include "cipher.h"


int main(int argc, char *argv[]){
	if (argc != 3){
		cerr << "Invalid amount of arguments\n";
	}
	else{
		vector<string> message; //potentially decrypted message
		vector<string> bank;
		string temp;
		string c = argv[1];
		string fileName = argv[2];
		int k = 1;
		
		bool decrypted = false;
		
		message = handler(c); // stores input string into string vector
		vector<string> original = message;
		
		ifstream file(fileName);
		
		if(file.is_open()){
			while (file >> temp){
				bank.push_back(temp); // reads file and stores into a string vector
			}
			file.close();
		}
		else{
			cerr << "File did not open properly\n";
			return -1;
		}
	
		for (int i = 1; i < 26; i++){	
			message = original;
			decrypt(message, i); //decrypts message as a signed char vector
			
			for(int j = 0; j < message.size(); j++){
			cout << message[j] << " ";
			}
			
			cout << endl;
			
			for(const auto& temp : message){
				if(find(bank.begin(), bank.end(), temp) != bank.end()){
					k = i;
					i = 26;
					break;
				}
			}
		}
		
		cout << "Decrypted Message: ";
		for (int x = 0; x < message.size(); x++){
			cout << message[x] << " ";
		}
		cout << endl;
		
		cout << "Key: " << k << endl;
	
	}

	return 0;
}
