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
On Windows, win32clipboard and win32con are required, and there are all included in pywin32:
	pip install pywin32
	
"""
import platform
import re
import time


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

        # p = Popen('xsel', shell=True, stdout=PIPE)
        # out = (p.stdout.readlines())[0] //oneline
        out = (Popen(['xsel'], shell=True, stdout=PIPE).communicate())[0]
        return out

    return copyL, pasteL


def winclipboard():
    import win32clipboard as wc
    import win32con
    def copyW(str):
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
        wc.CloseClipboard()

    def pasteW():
        wc.OpenClipboard()
        if wc.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            out = wc.GetClipboardData(win32con.CF_UNICODETEXT)
        else:
            out = ""
        wc.CloseClipboard()
        return out

    return copyW, pasteW


def newstr1(matched):
    newstr = matched.group('value')
    newstr = newstr[-1]
    return newstr


def newstr2(matched):
    newstr = matched.group('value')
    newstr = newstr[0] + " " + newstr[-1]
    return newstr


def newstr_e(matched):
    newstr = matched.group('value')
    newstr = " " + newstr[-1]
    return newstr


def removebreak(copy_text):
    # print(copy_text,type(copy_text),'\n')

    p1 = re.compile('(?P<value>-(\n|\r|\r\n)[a-z])')  # such as "commun-\nication"
    copy_text = re.sub(p1, newstr1, copy_text)
    # copy_text = re.sub(p1," ", copy_text)
    p2 = re.compile('(?P<value>[,\w](\n|\r|\r\n)[A-Z])')  # such as "we think that\n TCP is good enough to ..."
    copy_text = re.sub(p2, newstr2, copy_text)

    p_e = re.compile('(?P<value>(\n|\r|\r\n)\s*[^A-Z])')  # such as "... to finsh some\n works like ..."
    copy_text = re.sub(p_e, newstr_e, copy_text)

    # print(copy_text,type(copy_text),'\n')

    return copy_text


def get_copy_paste(sysstr):
    if sysstr == "Windows":
        copy, paste = winclipboard()
    else:
        copy, paste = linuxclipboard()
    return copy, paste


if __name__ == "__main__":
    sysstr = platform.system()
    copy, paste = get_copy_paste(sysstr)
    last_text = paste()
    while True:
        copy_text = paste()
        if last_text != copy_text:
            copy_text = removebreak(copy_text)
            copy(copy_text)
            last_text = copy_text
            print('done')
        else:
            time.sleep(0.2)
