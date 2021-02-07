# Principle
## NoteBook
`NoteBook`的`note.db`文件内有表`Note`，下有14列，分别为
`id` `audioPath` `content` `localVersion` `noteUUID` `recyclebin` `recyclebinVersion` `serverNoteId` `summary` `time` `title` `type` `updateTime` `uuid`

应用通过读写此表内14列来记录读取笔记内容。

其中`content`与`summary`都用于储存文本内容和格式信息，两者不同为`content`储存html格式文本，而`summary`储存纯文本(将回车替换为空格)，两者文本内容必须完全一致;
`audioPath`为笔记内录音文件地址，若无录音则为空;`id`为序列号;`noteUUID`为笔记UUID。

所以我们可以使用一些库获取必须的参数:
```python
escapedCharacter = [ "<", ">", "&", "\'", "\"", "\n", "\u00a0", "\u00ad" ]
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
