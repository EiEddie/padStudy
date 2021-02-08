# padStudy
某不知名电子垃圾内应用的读写

## 1.NoteBook
通过调用以下函数写入:
```python
StudyNoteIn(noteContent, noteTitle, noteCategory)
```
其中`noteContect`为正文; `noteTitle`为标题，默认为空; `noteCategory`为科目，默认为1:语文，对应关系如下:
>1:语文  
2:数学  
3:英语  
4:物理  
5:化学  
6:生物  
7:政治  
8:地理  
9:历史  
10:其他

同理通过调用以下函数读取笔记:
```python
StudyNoteOut(noteTitle)
```
`noteTitle`即为标题，函数返回一个列表

使用前请先按以下方法指定文件位置
```python
conn = sqlite3.connect('FilePath')
note = conn.cursor()#打开文件并设置游标
#在这里调用函数
conn.commit()
note.close()
conn.close()#关闭游标并关闭文件
```

## 2.UserHome
调用以下函数写入:
```python
StudyUserHomeIn(usFilePath, usClassName)
```
其中`usFilePath`为文件地址; `usClassName`为科目

请注意此函数仅修改`database`文件，调用时请将`UserHomeFile`文件夹内文件转移到`/padStudy01/UserHome/video`文件夹
```python
shutil.copyfile(
	usFilePath,r"UserHomeFile\%s"%usFileName
)#复制并改名
```
同理使用前请先按以下方法指定文件位置
```python
conn = sqlite3.connect('FilePath')
userHome = conn.cursor()#打开文件并设置游标
#在这里调用函数
conn.commit()
userHome.close()
conn.close()#关闭游标并关闭文件
```
