# Principle
## NoteBook
### In
`NoteBook`的`note.db`文件内有表`Note`，下有14列，分别为
`id` `audioPath` `content` `localVersion` `noteUUID` `recyclebin` `recyclebinVersion` `serverNoteId` `summary` `time` `title` `type` `updateTime` `uuid`

应用通过读写此表内14列来记录读取笔记内容

其中`content`与`summary`都用于储存文本内容和格式信息，两者不同为`content`储存html格式文本，而`summary`储存纯文本(将回车替换为空格)，两者文本内容必须完全一致; `audioPath`为笔记内录音文件地址，若无录音则为空; `id`为序列号; `noteUUID`为笔记UUID

所以我们可以使用一些库中的函数获取必须的参数:
```python
import time, uuid, random

escapedCharacter = [ "<", ">", "&", "\'", "\"", "\n", " ", "\u00ad" ]
scapeCharacter = [ "&lt;", "&gt;", "&amp;", "&apos;", "&quot;", "<br>", "&nbsp;", "&shy;" ]
#特殊字符

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
	random.randint(97,122))
```
之后用SQL语句写入`note.db`文件内:
```SQL
INSERT INTO Note VALUES(null,
                       "",
                       <noteContent>,
                       <noteLocalVersion>,
                       <noteUUID>,
                       0,
                       "",
                       0,
                       <noteSummary>,
                       <noteTime>,
                       <noteTitle>,
                       1000,
                       <noteTime>,
                       "")
```
同样地，如果我们修改`audioPath`即可插入音频，修改`recyclebin`即可移动到回收站内

此外，我们还需要将刚刚写入的笔记记录到`Category_Note`表中

首先通过`noteUUID`变量获取笔记的`id`值:
```SQL
SELECT id FROM Note WHERE noteUUID=<noteUUID>
```
将获得的`id`值记录在变量`noteId`中后，利用其作为中间变量将`id`值插入`Category_Note`表中:
```SQL
INSERT INTO Category_Note VALUES(<noteCategory>,
                                 <noteId>)
```

### Out
同样使用SQL语句读出指定笔记html格式文本:
```SQL
SELECT content FROM Note WHERE title=<noteTitle>
```
并将文本储存在列表`noteText`中

定义函数`noteHtmlToText()`将html格式文本转为纯文本:
```python
import re

escapedCharacter = [ "<", ">", "&", "\'", "\"", "\n", " ", "\u00ad" ]
scapeCharacter = [ "&lt;", "&gt;", "&amp;", "&apos;", "&quot;", "<br>", "&nbsp;", "&shy;" ]
#特殊字符

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
```
依次读取列表`noteText`中字符串，使用`noteHtmlToText()`转义后将其添加到列表`noteContentList`中:
```python
for i in noteText:
#读取正文
	noteContentList.append(
		noteHtmlToText(tuple(i)[0])
	)#转义
```
即可得到所有符合条件的正常格式的文本，储存在列表`noteContentList`中

## UserHome
这个稍微简单一点。。

它同样是利用数据库来储存下载内容信息的，储存在`userdata.db`文件中的`lessonResource`表内，其下有14列，分别为
`id` `filetype` `uuid` `filepath` `zipname` `homework` `filecount` `datetime` `filelist` `filesize` `maxversion` `classname` `type` `autosend`

应用通过读取这14列记录文件信息

其中`filepath`为文件在文件夹内的名字(包括扩展名); `homework`为文件原名(同样带扩展名); `datetime`为文件下载时时间; `filesize`为文件大小(单位Bit); `classname`为所属学科

我们首先利用一些函数获取所需参数

因不知道原应用`filepath`的命名方式是什么，我使用了文件哈希值，下为哈希算法:
```python
import hashlib

def UsHash(usFilePath, Bytes=1024):
	#获取文件哈希值(网上找的)
	usMd5 = hashlib.md5()
	with open(usFilePath,"rb") as usFile:
		while True:
			usFileData = usFile.read(Bytes)
			if usFileData:
				usMd5.update(usFileData)
			else:
				break
	usHash = usMd5.hexdigest()
	return usHash
```
但经过我反复实验后发现，使用哪种编码命名都不会影响文件的读取...

于是干脆对被导入文件的地址求哈希值，可以极大减小时间复杂度  
  
接下来就可以对所需变量赋值了:
```python
import os, time

usHomeWork = os.path.basename(usFilePath)
usFileSize = os.path.getsize(usFilePath)
usTime = int(round(time.time()*1000))
usFileExtension = os.path.splitext(usFilePath)[-1]
usFileName = UsHash(
	usFilePath) + usFileExtension
```
一如既往地，我们用SQL语句写入`userdata.db`文件中:
```SQL
INSERT INTO lessonResource VALUES(null,
                                 "",
                                 "",
                                 <usFileName>,
                                 "",
                                 <usHomeWork>,
                                 0,
                                 <usTime>,
                                 "",
                                 <usFileSize>,
                                 "",
                                 <usClassName>,
                                 "",
                                 "")
```
比较特殊的是，我们同样需要将重命名为`usFileName`的文件一并拷入到应用下的`/userhome/video`文件夹内，因此我们可以添加以下语句:
```python
import shutil

shutil.copyfile(
	usFilePath,r"UserHomeFile\%s"%usFileName
)#复制并改名
```
它可以将文件重命名后复制到我们所指定的文件夹内，方便后续我们手动将其拷入应用下的文件夹
