import sqlite3
import time, hashlib
import os, shutil

#def UsHash(usFilePath, Bytes=1024):
#	#获取文件哈希值
#	usMd5 = hashlib.md5()
#	with open(usFilePath,"rb") as usFile:
#		while True:
#			usFileData = usFile.read(Bytes)
#			if usFileData:
#				usMd5.update(usFileData)
#			else:
#				break
#	usHash = usMd5.hexdigest()
#	return usHash

def StudyUserHomeIn(usFilePath, usClassName="其它"):
	usHomeWork = os.path.basename(usFilePath)
	usFileSize = os.path.getsize(usFilePath)
	usTime = int(round(time.time()*1000))
	usFileExtension = os.path.splitext(usFilePath)[-1]
	usMd5 = hashlib.md5()
	usMd5.update(bytes(usFilePath,"utf-8"))
	usHsah = usMd5.hexdigest()
	usFileName = usHash + usFileExtension
	#变量赋值

	userHome.execute(
		'''INSERT INTO lessonResource VALUES(
						null,
						"",
						"",
						"{0}",
						"",
						"{1}",
						0,
						{2},
						"",
						{3},
						"",
						"{4}",
						"",
						"")'''
		.format(usFileName, 
			usHomeWork, 
			usTime, 
			usFileSize, 
			usClassName)
	)#写入

	shutil.copyfile(
		usFilePath,r"UserHomeFile\%s"%usFileName
	)#复制并改名

conn = sqlite3.connect('userdata.db')
userHome = conn.cursor()#打开文件并设置游标
#if __name__ == "__main__":

conn.commit()
userHome.close()
conn.close()#关闭游标并关闭文件
