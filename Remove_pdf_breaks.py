"""
Remove_pdf_breaks

A cross-platform pdf copy tools, with copy & paste functions for plain text.
If you want to translate something from PDF, it is usefull.

By lsyer(lishao378@sohu.com)
Thanks: Remove-line-breaks(https://github.com/symaeh/Remove-line-breaks-)

BSD License

Usage:
  1) Copy some paragraphies from PDF;
  2) Run this py script in the terminal.
  OK, go to paste where you want. 

On Linux, install xsel via package manager. For example, in Ubuntu:
    sudo apt-get install xsel
On Windows, win32clipboard and win32con are required:
	pip install win32clipboard
	pip install win32con
	
"""
import platform
import re

def linuxclipboard():
	def copyL(str, p=True, c=True):
		from subprocess import Popen, PIPE

		if p:
			p = Popen(['xsel', '-pi'], stdin=PIPE)
			p.communicate(input=str)
		if c:
			p = Popen(['xsel', '-bi'], stdin=PIPE)
			p.communicate(input=str)

	def pasteL():
		from subprocess import Popen, PIPE

		#p = Popen('xsel', shell=True, stdout=PIPE)
		#out = (p.stdout.readlines())[0] //oneline
		out = (Popen(['xsel'],shell=True,stdout=PIPE).communicate())[0]
		return out
		
	return copyL,pasteL

def winclipboard():
	import win32clipboard as wc
	import win32con
	
	def copyW(str):
		wc.OpenClipboard()
		wc.EmptyClipboard()
		wc.SetClipboardData(win32con.CF_TEXT, str)
		wc.CloseClipboard()

	def pasteW():
		wc.OpenClipboard()
		out = wc.GetClipboardData(win32con.CF_TEXT)
		wc.CloseClipboard()
		return out
		
	return copyW,pasteW
	
global copy, paste
sysstr = platform.system()
if(sysstr =="Windows"):
	copy, paste = winclipboard()
else:
	copy, paste = linuxclipboard()

copy_text = paste()

#print(copy_text,type(copy_text),'\n')
print(copy_text)

p1 = re.compile(r'[(\n)(\r)(\r\n)][\s+]')
p2 = re.compile(r'[(\n)(\r)(\r\n)]')
copy_text = re.sub(p1,'<br>',copy_text)
copy_text = re.sub(p2,' ',copy_text)

#copy_text = copy_text.replace(b'\r\n',b' ')
#copy_text = copy_text.replace(b'\n',b' ')
#copy_text = copy_text.replace(b'\r',b' ')
copy_text = copy_text.replace(b'- ',b'')
copy_text = copy_text.replace(b'<br>',b'\r\n ')

#print(copy_text,type(copy_text),'\n')
print(copy_text)

copy(copy_text)
print('done')
