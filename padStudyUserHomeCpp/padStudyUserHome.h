#pragma once
#include<iostream>
#include<fstream>
#include<string>
#include<time.h>
//#include<sqlite3.h>
using namespace std;

void StrReplace(string&, const string&, const string&);
string GetFileName(string);
string GetFileExtension(string);
unsigned int GetFileSize(const string&);
int64_t GetTime(void);
void StudyUserHomeIn(string, string usClassName="其它");