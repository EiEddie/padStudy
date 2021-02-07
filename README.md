# padStudy
某不知名电子垃圾内应用的读写

## 1.NoteBook
通过调用函数
```python
StudyNoteIn(noteContent, noteTitle)
```
实现写入，
同理通过调用函数
```python
StudyNoteOut(noteTitle)
```
实现读取
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
调用函数
```python
StudyUserHomeIn(usFilePath, usClassName)
```
写入，
请注意此函数仅修改`database`文件，调用时请修改以下源码语句选择合适文件夹并将其内文件转移到`/padStudy01/UserHome/video`文件夹内
```python
shutil.copyfile(
	usFilePath,"/storage/emulated/0/%s"%usFileName
)#复制并改名(文件夹请自行设置!)
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
