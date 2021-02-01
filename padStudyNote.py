import sqlite3
import uuid, time
import random

escapedCharacter = [ "<", ">", "&", "\'", "\"", "\n", "\u00a0", "\u00ad" ]
scapeCharacter = [ "&lt;", "&gt;", "&amp;", "&apos;", "&quot;", "<br>", "&nbsp;", "&shy;" ]
#特殊字符

def StudyNoteIn(noteContent="", noteTitle="title"):
	#写入函数
	for i in range(0,8):
		noteContent = noteContent.replace(
			escapedCharacter[i], scapeCharacter[i]
		)
	noteSummary = noteContent.replace("<br>", " ")
	#特殊字符转义

	noteUUID = "".join(str(uuid.uuid4()).split("-"))
	noteTime = int(round(time.time()*1000))
	noteLocalVersion = "0."+ chr(
		random.randint(97,122)) + chr(
		random.randint(97,122))#变量赋值

	note.execute(
		'''INSERT INTO Note VALUES(null,"null","{0}","{1}","{2}",0,"",0,"{3}",{4},"{5}",1000,{4},"")'''
		.format(noteContent,noteLocalVersion,noteUUID,noteSummary,noteTime,noteTitle)
	)#写入正文

	note.execute(
		'''SELECT id FROM Note WHERE localVersion="{0}"'''
		.format(noteLocalVersion)
	)
	noteId = note.fetchall()
	note.execute(
		'''INSERT INTO Category_Note VALUES("1","{0}")'''
		.format(tuple(noteId[0])[0])
	)#记录到Category_Note表中


def StudyNoteOut(noteTitle):
	#读取函数
	note.execute(
		'''SELECT content FROM Note WHERE title="{0}"'''
		.format(noteTitle)
	)
	noteText = note.fetchall()
	noteContent = tuple(noteText[0])[0]
	#读取正文

	for i in range(0,8):
		noteContent = noteContent.replace(
			scapeCharacter[i], escapedCharacter[i]
		)#特殊字符转义
	return noteContent

conn = sqlite3.connect('/storage/emulated/0/储存/临时/padStudy01/note.db')
note = conn.cursor()#打开文件并设置游标
#if __name__ == "__main__":

conn.commit()
note.close()
conn.close()#关闭游标并关闭文件
