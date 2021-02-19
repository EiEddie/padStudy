#include"padStudyUserHome.cpp"
//#include<sqlite3.h>

int main(int argc, char *argv[]) {
	cout << " FilePath: \n";
	string filePath;
	getline(cin, filePath);
	cout << " StorageLocation: \n";
	string fileClassName;
	getline(cin, fileClassName);
	StudyUserHomeIn(filePath, fileClassName);
	return 0;
}