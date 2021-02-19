/*#include<iostream>
#include<fstream>
#include<string>
#include<time.h>
using namespace std;*/
#include"padStudyUserHome.h"

void StrReplace(string& originalStr, const string& strSrc, const string& strDst) {
	string::size_type pos = 0;
	string::size_type srcLen = strSrc.size();
	string::size_type dstlen = strDst.size();
	while((pos=originalStr.find(strSrc, pos)) != string::npos) {
		originalStr.replace(pos, srcLen, strDst);
		pos += dstlen;
	}
}

unsigned int GetFileSize(const string& filePath) {
	ifstream in(filePath.c_str());
	in.seekg(0, ios::end);
	size_t size = in.tellg();
	in.close();
	return size;
}

string GetFileName(string filePath) {
	StrReplace(filePath, "/", "\\");
	if (filePath.empty()) return "";
	string::size_type iPos = filePath.find_last_of('\\') + 1;
	return filePath.substr(iPos, filePath.length() - iPos);
}

string GetFileExtension(string fileName) {
	return fileName.substr(fileName.find_last_of('.'));
}

int64_t GetTime(void) {
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}