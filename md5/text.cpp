#include"md5.cpp"
#include<iostream>
using namespace std;

void PrintMD5(const string& str, MD5& md5) {
	cout << "MD5(" << str << ") = " << md5.toString() << endl;
}

int main() {
	MD5 md5;
	md5.update("hsjdhwk");
	PrintMD5("hsjdhwk", md5);
	return 0;
}
