/*#include"padStudyUserHome.h"
#include<iostream>
#include<fstream>
#include<sqlite3.h>
using namespace std;*/
#include"variable.cpp"
#include"../md5/md5.cpp"
#include<sqlite3.h>

static int callback(void*, int, char**, char**);

void StudyUserHomeIn(string usFilePath,
		string usClassName) {
	sqlite3 *db;
	char* zErrMsg = 0;
	int temp = sqlite3_open("../userdata.db", &db);
	if(temp) {
		cout << " Open database unsuccessfully: " 
			<< sqlite3_errmsg(db) << endl;
		return;
	} else {
		cout << " Open successfully\n";
	}

	MD5 fileHash;
	fileHash.update(usFilePath);
	string usFileName = fileHash.toString() +
		GetFileExtension(GetFileName(usFilePath));
	string strSql = "INSERT INTO lessonResource VALUES(null,'','','" +
	GetFileName(usFilePath) +
	"','','" +
	usFileName +
	"',0,"+
	to_string(GetTime()) +
	",''," +
	to_string(GetFileSize(usFilePath)) +
	",'','" +
	usClassName +
	"','','');";
	const char* sql = strSql.c_str();
	temp = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
	if(temp != SQLITE_OK) {
		cout << " SQL error: " << zErrMsg << endl;
		sqlite3_free(zErrMsg);
		return;
	} else {
		cout << " Write in successfully\n";
	}
	sqlite3_close(db);

	ifstream in(usFilePath.c_str(), ios::binary);
	string a = "../UserHomeFile/";
	ofstream out((a+usFileName).c_str(), ios::binary);
	if(!in || !out) {
		cout << " Copy file unsuccessfully\n";
		return;
	} else {
		cout << " Copy file successfully\n";
	out << in.rdbuf();
	in.close();
	out.close();
}

static int callback(void* NotUsed,
		int argc,
		char** argv,
		char** azColName) {
/*	for(int i=0; i<argc; i++){
		printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
	}
	printf("\n");*/
	return 0;
}