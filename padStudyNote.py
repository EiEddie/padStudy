import sqlite3
import uuid, time
import random, re

escapedCharacter = [ "<", ">", "&", "\'", "\"", "\n", " ", "\u00ad" ]
scapeCharacter = [ "&lt;", "&gt;", "&amp;", "&apos;", "&quot;", "<br>", "&nbsp;", "&shy;" ]
#特殊字符

def StudyNoteIn(noteContent="", noteTitle="title", noteCategory="1"):
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
		'''INSERT INTO Note VALUES(
					null,
					"null",
					"{0}",
					"{1}",
					"{2}",
					0,
					"",
					0,
					"{3}",
					{4},
					"{5}",
					1000,
					{4},
					"")'''
		.format(noteContent,
			noteLocalVersion,
			noteUUID,
			noteSummary,
			noteTime,
			noteTitle)
	)#写入正文
	note.execute(
		'''SELECT id FROM Note WHERE noteUUID="{0}"'''
		.format(noteUUID)
	)
	noteId = note.fetchall()
	note.execute(
		'''INSERT INTO Category_Note VALUES(
						"{0}",
						"{1}")'''
		.format(noteCategory, 
			tuple(noteId[0])[0])
	)#记录到Category_Note表中

def noteHtmlToText(noteContent):
	#转义函数
	noteContent = re.sub(
		r"<(?!br).*?>", "", noteContent
	)
	for i in range(0,8):
		noteContent = noteContent.replace(
			scapeCharacter[i], escapedCharacter[i]
		)
	return noteContent

def StudyNoteOut(noteTitle):
	#读取函数
	noteContentList = []
	note.execute(
		'''SELECT content FROM Note WHERE title="{0}"'''
		.format(noteTitle)
	)
	noteText = note.fetchall()
	for i in noteText:
	#读取正文
		noteContentList.append(
			noteHtmlToText(tuple(i)[0])
		)#转义
	return noteContentList

conn = sqlite3.connect('/storage/emulated/0/储存/临时/padStudy01/note.db')
note = conn.cursor()#打开文件并设置游标
#if __name__ == "__main__":

conn.commit()
note.close()
conn.close()#关闭游标并关闭文件
