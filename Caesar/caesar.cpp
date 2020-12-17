#include <iostream>
#include <string>
using namespace std;


string caesar(string plaintext,int key) {
	string result;
	for (int i = 0; i < plaintext.length();i++) {
		int aa = (int)plaintext[i];
		if ( 64 < aa && aa < 91 ) {
			aa += key;
			if (aa > 90) {
				aa = 64 + (aa - 90);
			}
		}
		else if (96 < aa && aa < 123) {
			aa += key;
			if (aa > 122) {
				aa = 96 + (aa - 122);
			}
		}
		result += (char)aa;
	}
	return result;
} 

int main(int argc, char* argv[]) {
	char* p;
	if (argc != 2) return 0;
	long key = strtol(argv[1], &p, 10) % 26;
	string plaintext;
	cout << "plaint text:";
	getline(cin, plaintext);
	cout << "chipper text:" << caesar(plaintext, key) << endl;
	return 0;
}

